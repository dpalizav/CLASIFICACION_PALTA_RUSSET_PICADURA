# Clasificacion de defectos superficiales en palta Hass

Clasificacion binaria PICADURA y RUSSET con ResNet50 y Transfer Learning.

## Datos

Cada TIFF representa una palta con tres franjas de camaras. Las franjas muestran hasta 30 vistas del mismo fruto. Las vistas se conservan juntas; no se consideran 30 muestras independientes.

El dataset no esta dentro del repositorio. La disposicion utilizada es:

```text
Carpeta de trabajo/
  DATASET_PALTA/
    train/PICADURA/
    train/RUSSET/
    validation/PICADURA/
    validation/RUSSET/
    test/PICADURA/
    test/RUSSET/
  PROYECTO_TI_2/
```

En los notebooks de entrenamiento la ruta relativa es `../DATASET_PALTA`. No cambiar las particiones ni los TIFF originales.

## Archivos principales

| Archivo | Uso |
|---|---|
| `4. EDA/01_EDA.ipynb` | Inventario, clases, calidad y duplicados. |
| `5. feature_engineering/feature_engineering_palta.ipynb` | Transformaciones y descriptores de imagen. |
| `6. entrenamiento/resnet50.ipynb` | Baseline, resolucion, balanceo y fine-tuning opcional. |
| `2. informe/Informe.ipynb` | Informe con tablas y figuras que lee las metricas guardadas. |
| `7. resultados/` | EDA, FE y corridas de clasificacion. |
| `utilidades_imagenes.py` | Lectura TIFF y resize proporcional. |

## Estado de los experimentos

El EDA registro 829 archivos y dos pares exactos entre particiones. La auditoria de entrenamiento verifico los hashes y excluyo cuatro rutas de las listas experimentales. Quedaron 572 archivos de train, 127 de validation y 126 de test reservado.

El Feature Engineering se ejecuto con 24 imagenes de entrenamiento. B0 y V1 tienen resultados reales de ResNet50 congelada sobre validation:

| Corrida | Entrada | Macro-F1 | Recall RUSSET |
|---|---|---:|---:|
| B0 | 256 x 512 | 0.6604 | 0.3333 |
| V1 | 384 x 768 | 0.6598 | 0.2857 |

Las nuevas condiciones D1 y D2 estan preparadas, pero aun requieren ejecucion con los TIFF locales:

- D1: una copia fotometrica por fruto RUSSET, sin escribir archivos de imagen.
- D2: dos copias fotometricas por fruto RUSSET, con el mismo procedimiento.
- FT_B0 y FT_D1: ajuste fino parcial del bloque conv5, opcional y solo despues de entrenar la cabeza correspondiente.

El volteo horizontal V2 no se utiliza: cambia el orden de las vistas dentro de las franjas. Validation y test nunca reciben augmentation.

## Ejecucion en VS Code

1. Abrir la carpeta `PROYECTO_TI_2`, junto al dataset original.
2. Abrir `6. entrenamiento/resnet50.ipynb` y seleccionar `Python (palta TensorFlow)`.
3. Ejecutar el notebook con `ENTRENAR = False`, `REVISAR_INTEGRIDAD = False` y `EJECUTAR_FT = False`.
4. Revisar los cuatro archivos propuestos para excluir. Activar `REVISAR_INTEGRIDAD = True` y, tras revisar, `APROBAR_EXCLUSIONES = True` para comprobar los SHA-256.
5. Elegir `CONDICION = "D1"`, activar `ENTRENAR = True` y ejecutar solamente la celda de control. Los pesos de ImageNet pueden descargarse la primera vez.
6. Desactivar `ENTRENAR` al terminar. Ejecutar D2 si se necesita la segunda variante.
7. Si se hara fine-tuning, utilizar el control separado `EJECUTAR_FT` y comenzar con FT_B0. La corrida B0 congelada y su archivo de pesos deben estar presentes.
8. Abrir `2. informe/Informe.ipynb` y ejecutar Run All para actualizar cuadros y graficos desde los CSV, JSON y PNG guardados.

Las corridas existentes no se sobrescriben. Para repetir una condicion usar otra `REPETICION` sin borrar resultados previos.

## CPU y GPU

El entorno anterior utilizo Python 3.11 y TensorFlow 2.21 en Windows. CPU es suficiente para probar D1 y D2, aunque extraer caracteristicas lleva tiempo.

Si existe una GPU NVIDIA compatible, comprobar primero el resultado de la seccion `Comprobar GPU` del notebook. En Windows, TensorFlow 2.11 en adelante no usa GPU CUDA de manera nativa. Se recomienda configurar WSL2 y TensorFlow con soporte CUDA en un entorno separado. No modificar el entorno CPU que ya funciona hasta validar la instalacion nueva.

## Publicacion

No subir TIFF, copias aumentadas, dataset, entornos, cache de ImageNet ni checkpoints del modelo. Los archivos `.h5`, `.keras`, TIFF y `.venv` estan excluidos en `.gitignore`.

Repositorio: https://github.com/dpalizav/CLASIFICACION_PALTA_RUSSET_PICADURA
