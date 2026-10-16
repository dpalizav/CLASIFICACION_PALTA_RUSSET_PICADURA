# Clasificación de defectos en palta Hass mediante visión por computadora

**Autor:** Luis Daniel Paliza Vilca  
**Etapa actual:** Feature Engineering  
**Modelo principal:** ResNet50 mediante Transfer Learning, con TensorFlow/Keras.

## Objetivo

Preparar imágenes de palta Hass para diferenciar las clases PICADURA y RUSSET.
Cada archivo contiene una palta con tres franjas de cámaras y vistas por rotación.
Las vistas de un mismo fruto conservan su etiqueta y partición; no son muestras
independientes. La entrega actual prepara características y entradas para el modelo,
sin entrenamiento.

## Organización

| Ubicación | Contenido |
|---|---|
| `1. fuentes/` | Bitácora técnica actualizada. |
| `2. informe/` | Carpeta existente conservada, vacía en el adjunto. |
| `3. presentacion/` | Carpeta existente conservada, vacía en el adjunto. |
| `4. EDA/01_EDA.ipynb` | Inventario, distribución, calidad, duplicados y leakage. |
| `4. EDA/ejecutar_eda.py` | Ejecutor del EDA; guarda el notebook solo si termina correctamente. |
| `5. feature_engineering/feature_engineering_palta.ipynb` | Tamaño, normalización, RGB/HSV, brillo, contraste, histogramas, textura y preparación para ResNet50. |
| `6. entrenamiento/resnet50.ipynb` | Baseline existente adaptado a ResNet50; funciones futuras sin llamadas automáticas. |
| `7. resultados/eda/` | Cinco reportes históricos del EDA. |
| `7. resultados/feature_engineering/` | Destino de tablas y configuración al ejecutar FE con imágenes. |
| `utilidades_imagenes.py` | Rutas portables, lectura TIFF, resize con relleno y carga por lotes. |
| `requirements.txt` | Dependencias básicas de EDA y FE. |
| `requirements_resnet50.txt` | Dependencias adicionales del pipeline TensorFlow y las métricas futuras. |
| `CAMBIOS.md` | Archivos modificados, nuevos, movidos y conservados; alcance de la validación. |

El **EDA comprende y audita** los datos. **Feature Engineering transforma y prepara**
su representación. Las estadísticas de color del EDA siguen siendo diagnósticas;
la preparación de entradas y descriptores está en el notebook de FE.

## Dataset y rutas

El RAR no contiene los TIFF. Mantener `DATASET_PALTA` en su ubicación actual, dentro
o junto a la carpeta del proyecto. Debe conservar estas rutas:

- `DATASET_PALTA/train/PICADURA/` y `DATASET_PALTA/train/RUSSET/`.
- `DATASET_PALTA/validation/PICADURA/` y `DATASET_PALTA/validation/RUSSET/`.
- `DATASET_PALTA/test/PICADURA/` y `DATASET_PALTA/test/RUSSET/`.

La búsqueda funciona desde la raíz o la carpeta del notebook. Si hay dos copias,
seleccionar una ruta relativa: `"../DATASET_PALTA"` o `"DATASET_PALTA"` en
`RUTA_DATASET_RELATIVA`; en el EDA la variable se llama `RUTA_DATASET_MANUAL`.
No se crean particiones ni se mueve, renombra o sobrescribe ninguna imagen.

## Ejecución en VS Code

Usar Python 3.12. Abrir una terminal en la raíz del proyecto:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Seleccionar `.venv` como kernel en VS Code, con la extensión Jupyter.
En Linux/macOS se pueden usar `python3 -m venv .venv` y
`.venv/bin/python -m pip install -r requirements.txt`.

1. Leer `4. EDA/01_EDA.ipynb`: conserva tablas y gráficos de la ejecución histórica.
2. Abrir `5. feature_engineering/feature_engineering_palta.ipynb` y ejecutar las celdas
   en orden. Con el dataset disponible, toma hasta 12 archivos por clase de train.
   Sin el dataset, muestra los pendientes y no genera resultados ficticios.
3. Para verificar un lote con TensorFlow, instalar las dependencias adicionales:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements_resnet50.txt
```

FE comprueba la equivalencia del preprocesamiento cuando TensorFlow está instalado.
La extracción profunda queda desactivada con `EXTRAER_CARACTERISTICAS_PROFUNDAS = False`.
Ejecutar todo en `resnet50.ipynb` solo define funciones; no inicia entrenamiento ni
descarga pesos. No hace falta una GPU para el avance de FE.

Para recalcular el EDA con el dataset local:

```powershell
.\.venv\Scripts\python.exe "4. EDA\ejecutar_eda.py"
```

La ejecución actualiza los cinco reportes `eda_*` en `7. resultados/eda/`. FE guarda
sus tablas y configuración en `7. resultados/feature_engineering/`. Todos los cambios
de tamaño y color ocurren en memoria; los originales permanecen intactos.

## Decisiones de preparación

- Entrada inicial: **256 × 512 píxeles, alto × ancho**, con proporción conservada y
  relleno. Mantiene las tres franjas; aún falta validar detalle de defectos pequeños.
- RGB `[0, 1]` se usa para descriptores. ResNet50 recibe RGB `float32` `[0, 255]` y
  aplica su `preprocess_input` una vez, dentro del modelo. No combinar ambos escalados.
- Histogramas, HSV y GLCM son características descriptivas; no se concatenan al modelo.
- Volteo horizontal propuesto solo para train, sujeto a revisión visual. Validación y
  test permanecen deterministas. No se generan copias físicas aumentadas.

## Estado actual

El EDA adjunto documenta **829 imágenes**, PICADURA: 710 y RUSSET: 119, y **dos pares
exactos entre particiones**, uno con etiquetas contradictorias. Son resultados
históricos del 9 de octubre de 2026, conservados sin recalcular durante esta revisión.
No se ha demostrado independencia por fruto/lote.

Feature Engineering está implementado y queda pendiente su ejecución sobre los TIFF
originales para obtener resultados del avance. Las pruebas técnicas de esta revisión
se describen en `CAMBIOS.md`; no sustituyen esa ejecución. El entrenamiento futuro
verifica la auditoría y permanece bloqueado por las incidencias registradas.

Antes de entrenar: revisar duplicados y etiquetas, documentar fruto/lote y procedencia,
validar tamaño y augmentation, y fijar evaluación por fruto. No ajustar decisiones
con test. Métricas previstas: F1 por clase, macro-F1, balanced accuracy y matriz de
confusión. La referencia histórica a MobileNetV3Small se conserva solo para explicar
la adaptación del baseline.
