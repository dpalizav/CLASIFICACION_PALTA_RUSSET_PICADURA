"""Rutas, lectura de TIFF y preparación común de las imágenes."""

from pathlib import Path, PureWindowsPath

import numpy as np
import pandas as pd
from PIL import Image, ImageOps


PARTICIONES = ("train", "validation", "test")
EXTENSIONES = {".tif", ".tiff", ".png", ".jpg", ".jpeg", ".bmp", ".webp"}
TAMANO_ENTRADA = (256, 512)  # Alto, ancho.


def encontrar_raiz(inicio=None):
    inicio = Path.cwd() if inicio is None else Path(inicio)
    inicio = inicio.resolve()
    for carpeta in (inicio, *inicio.parents):
        if (carpeta / "README.md").is_file() and (carpeta / "utilidades_imagenes.py").is_file():
            return carpeta
    raise FileNotFoundError("Abra el notebook desde la carpeta del proyecto o una subcarpeta.")


def resolver_dataset(raiz, ruta_relativa=None, requerido=True):
    raiz = Path(raiz)
    if ruta_relativa is not None:
        ruta = Path(ruta_relativa)
        ruta_windows = PureWindowsPath(str(ruta_relativa))
        if ruta.is_absolute() or ruta_windows.drive or ruta_windows.root:
            raise ValueError("La ruta del dataset debe ser relativa al proyecto.")
        if "\\" in str(ruta_relativa):
            raise ValueError("Use / o partes de pathlib para escribir una ruta portable.")
        candidatas = [(raiz / ruta).resolve()]
    else:
        candidatas = [raiz / "DATASET_PALTA", raiz.parent / "DATASET_PALTA"]

    disponibles = list(dict.fromkeys(p.resolve() for p in candidatas if p.is_dir()))
    if len(disponibles) > 1:
        raise ValueError("Hay dos DATASET_PALTA. Indique una ruta relativa explícita.")
    if not disponibles:
        if requerido:
            raise FileNotFoundError(
                "No se encontró DATASET_PALTA dentro o junto al proyecto. "
                "Mantenga el dataset original y revise RUTA_DATASET_RELATIVA."
            )
        return None

    dataset = disponibles[0]
    faltantes = [p for p in PARTICIONES if not (dataset / p).is_dir()]
    if faltantes:
        raise ValueError(f"Faltan particiones existentes: {', '.join(faltantes)}. No se crearán.")
    return dataset


def listar_imagenes(dataset, particion, clases=None):
    dataset = Path(dataset)
    if particion not in PARTICIONES:
        raise ValueError(f"Partición desconocida: {particion}")
    if clases is None:
        clases = sorted(p.name for p in (dataset / "train").iterdir() if p.is_dir())
    clases = list(clases)
    if not clases or len(clases) != len(set(clases)):
        raise ValueError("Revise las carpetas de clases del conjunto train.")
    presentes = {p.name for p in (dataset / particion).iterdir() if p.is_dir()}
    if presentes != set(clases):
        raise ValueError(f"Las clases de {particion} no coinciden con train: {sorted(presentes)}")

    registros = []
    for etiqueta, clase in enumerate(clases):
        carpeta = dataset / particion / clase
        for ruta in sorted(carpeta.rglob("*")):
            if ruta.is_file() and ruta.suffix.lower() in EXTENSIONES:
                archivo = ruta.relative_to(dataset).as_posix()
                registros.append({"archivo": archivo, "particion": particion,
                                  "clase": clase, "etiqueta": etiqueta, "id_archivo": archivo})
    columnas = ["archivo", "particion", "clase", "etiqueta", "id_archivo"]
    return pd.DataFrame(registros, columns=columnas)


def cargar_rgb(ruta):
    with Image.open(Path(ruta)) as imagen:
        if getattr(imagen, "n_frames", 1) != 1:
            raise ValueError("Revise el TIFF multipágina en el EDA antes de preparar su entrada.")
        return ImageOps.exif_transpose(imagen).convert("RGB").copy()


def ajustar_tamano(imagen, tamano=TAMANO_ENTRADA, color_relleno=(124, 117, 104)):
    alto, ancho = map(int, tamano)
    if alto < 32 or ancho < 32:
        raise ValueError("ResNet50 requiere al menos 32 píxeles por dimensión.")
    contenida = ImageOps.contain(imagen.convert("RGB"), (ancho, alto), Image.Resampling.LANCZOS)
    izquierda = (ancho - contenida.width) // 2
    arriba = (alto - contenida.height) // 2
    lienzo = Image.new("RGB", (ancho, alto), color_relleno)
    lienzo.paste(contenida, (izquierda, arriba))
    mascara = np.zeros((alto, ancho), dtype=bool)
    mascara[arriba:arriba + contenida.height, izquierda:izquierda + contenida.width] = True
    return np.asarray(lienzo, dtype=np.uint8).copy(), mascara


def crear_dataset_tf(tabla, dataset, tamano=TAMANO_ENTRADA, tamano_lote=8,
                     entrenamiento=False, semilla=42):
    """Entrega lotes RGB 0–255; el modelo aplica augmentation y preprocess_input."""
    import tensorflow as tf

    if tabla.empty:
        raise ValueError("No hay imágenes para crear el pipeline.")
    if entrenamiento and set(tabla["particion"]) != {"train"}:
        raise ValueError("Solo train puede usar el pipeline de entrenamiento.")
    if tamano_lote < 1:
        raise ValueError("El tamaño del lote debe ser positivo.")
    rutas = [str(Path(dataset) / archivo) for archivo in tabla["archivo"]]
    etiquetas = tabla["etiqueta"].to_numpy(dtype=np.int32)
    alto, ancho = map(int, tamano)

    def leer_array(ruta_bytes):
        ruta = ruta_bytes.item() if isinstance(ruta_bytes, np.ndarray) else ruta_bytes
        if isinstance(ruta, bytes):
            ruta = ruta.decode("utf-8")
        imagen = cargar_rgb(Path(ruta))
        matriz, _ = ajustar_tamano(imagen, tamano)
        return matriz.astype(np.float32)

    def preparar(ruta, etiqueta):
        matriz = tf.numpy_function(leer_array, [ruta], tf.float32)
        matriz.set_shape((alto, ancho, 3))
        etiqueta.set_shape(())
        return matriz, etiqueta

    flujo = tf.data.Dataset.from_tensor_slices((rutas, etiquetas))
    if entrenamiento:
        flujo = flujo.shuffle(len(tabla), seed=semilla, reshuffle_each_iteration=True)
    flujo = flujo.map(preparar, num_parallel_calls=2, deterministic=True)
    opciones = tf.data.Options()
    opciones.threading.private_threadpool_size = 2
    return flujo.with_options(opciones).batch(tamano_lote).prefetch(1)
