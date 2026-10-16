# Reorganización y avance de Feature Engineering

**Fecha de revisión:** 16 de octubre de 2026.  
**Entradas:** `Proyecto tesis.rar` y `bitacora_proyecto_clasificacion_palta.ipynb`.  
**Entrega:** carpeta `Proyecto_tesis` dentro de `Proyecto_tesis_feature_engineering.zip`.

## 1. Inspección inicial

El RAR contenía 11 archivos: dos notebooks, un ejecutor, cinco reportes y tres
archivos de configuración/documentación. Las carpetas `1. fuentes`, `2. informe`
y `3. presentacion` estaban vacías. El EDA y todos sus reportes estaban dentro
de `4. entrenamiento`. No existía una carpeta específica de Feature Engineering.

El baseline utilizaba `MobileNetV3Small` en sus textos y en la construcción de
la red; el README y el EDA ya identificaban ResNet50 como modelo principal.
La bitácora incluía rutas personales de Windows y un estado anterior cuya
siguiente entrega era el EDA.

`DATASET_PALTA` no estaba incluido. Los reportes históricos documentan 829 imágenes
de PICADURA y RUSSET, dos pares exactos entre particiones y un caso con etiquetas
contradictorias. Los criterios de bytes y píxeles producen cuatro filas de reporte,
pero corresponden a dos pares únicos. Estos resultados se conservaron; no se
atribuyen a una nueva ejecución sobre el dataset original.

## 2. Decisiones de organización

Se conservaron las tres carpetas documentales. Las etapas computacionales quedaron
ordenadas como `4. EDA`, `5. feature_engineering`, `6. entrenamiento` y `7. resultados`.
La carpeta antigua de entrenamiento quedó vacía después de trasladar todos sus
archivos y se retiró de la copia. No se borró ninguno de sus archivos útiles.

Se mantuvo el nombre `01_EDA.ipynb` para conservar continuidad. El baseline existente
se adaptó y renombró a `resnet50.ipynb`; no se creó un segundo notebook que duplicara
su función. La bitácora adjunta se incorporó a `1. fuentes`.

## 3. Archivos modificados

| Archivo actual | Cambio |
|---|---|
| `README.md` | Estructura real, EDA separado, etapa FE, ResNet50, dependencias, ejecución y límites de los resultados. |
| `requirements.txt` | Dependencias usadas por análisis, imágenes y ejecución de notebooks. Rangos de versiones compatibles en lugar de presentar los pines históricos como validados en esta revisión. |
| `.gitignore` | Conserva exclusiones originales y agrega dataset/configuración local. No oculta nuevas figuras de documentación. |
| `4. EDA/01_EDA.ipynb` | Rutas, destino de reportes, errores claros, referencias a FE, nota histórica y nombre neutral del kernel. Conserva todas las salidas originales. |
| `4. EDA/ejecutar_eda.py` | Guarda el notebook solo después de ejecución y validación correctas; un error no destruye sus salidas anteriores. |
| `6. entrenamiento/resnet50.ipynb` | Sustituye MobileNetV3Small por ResNet50, conserva lógica útil y deja entrenamiento/evaluación como funciones sin invocación automática. |
| `1. fuentes/bitacora_proyecto_clasificacion_palta.ipynb` | Actualiza rutas, estructura y etapa. Git queda documentado como antecedente, sin comandos automáticos. Agrega esta revisión. |

## 4. Archivos nuevos

| Archivo | Contenido |
|---|---|
| `5. feature_engineering/feature_engineering_palta.ipynb` | Las 15 secciones solicitadas, con 34 celdas: lectura, tamaño, normalización, RGB, brillo, contraste, histogramas, HSV, GLCM, augmentation y preparación para ResNet50. |
| `utilidades_imagenes.py` | Funciones comunes de rutas, carga TIFF/RGB, ajuste proporcional con relleno y pipeline por lotes. |
| `requirements_resnet50.txt` | TensorFlow para comprobar el pipeline y scikit-learn para las métricas del entrenamiento futuro. Incluye las dependencias básicas. |
| `CAMBIOS.md` | Este registro de modificaciones, conservación y validación. |

La bitácora es nueva dentro de la carpeta del proyecto, pero procede del segundo
adjunto del usuario; no se generó otra bitácora independiente.

## 5. Archivos movidos o renombrados

| Ubicación anterior | Ubicación actual |
|---|---|
| `4. entrenamiento/01_EDA.ipynb` | `4. EDA/01_EDA.ipynb` |
| `4. entrenamiento/ejecutar_eda.py` | `4. EDA/ejecutar_eda.py` |
| `4. entrenamiento/02_Baseline.ipynb` | `6. entrenamiento/resnet50.ipynb` |
| `4. entrenamiento/eda_inventario.csv` | `7. resultados/eda/eda_inventario.csv` |
| `4. entrenamiento/eda_calidad.csv` | `7. resultados/eda/eda_calidad.csv` |
| `4. entrenamiento/eda_duplicados.csv` | `7. resultados/eda/eda_duplicados.csv` |
| `4. entrenamiento/eda_distribucion.csv` | `7. resultados/eda/eda_distribucion.csv` |
| `4. entrenamiento/eda_resumen.json` | `7. resultados/eda/eda_resumen.json` |

## 6. Elementos conservados sin modificar

- **Los cinco reportes `eda_*`:** contenido idéntico byte a byte al RAR, verificado
  mediante SHA-256. Se conservan porque son evidencia de la ejecución histórica.
- **Las salidas del EDA:** todos los objetos `outputs` y contadores de ejecución se
  mantuvieron, incluidas sus 11 imágenes de salida. No se reemplazaron con resultados
  de pruebas temporales.
- **`2. informe/` y `3. presentacion/`:** permanecen vacías, como en el adjunto.
  `1. fuentes/` se conserva y ahora contiene la bitácora.
- **Los dos adjuntos originales:** permanecen intactos. Los cambios están en la copia.
- **Dataset original:** no disponible en los adjuntos y no modificado. No se
  agregaron imágenes de prueba a la entrega ni se reconstruyeron sus particiones.
- **Repositorio remoto e historial Git:** no se accedió al remoto ni se ejecutaron
  `git add`, `git commit`, `git push` o creación de ramas.

La carpeta `prueba/`, mencionada en el README anterior, tampoco venía en el RAR.
No se creó una carpeta vacía para simular que se había inspeccionado su contenido.

## 7. Cambios metodológicos del avance

El EDA conserva su función diagnóstica. El nuevo notebook toma una muestra reproducible
exclusivamente de train —hasta 12 archivos por clase— y prepara las imágenes en memoria.
Esta selección facilita revisar transformaciones; no balancea ni modifica el dataset.

La entrada inicial es de 256 × 512 píxeles, alto × ancho, conservando proporción y
todas las franjas mediante relleno. La máscara excluye el relleno de los descriptores,
pero incluye el fondo industrial original. El tamaño y el posible efecto del fondo
deben revisarse sobre las imágenes reales.

La normalización RGB a [0, 1] se utiliza para brillo, contraste, histogramas, HSV
y textura GLCM. La preparación de ResNet50 recibe RGB [0, 255], convierte a BGR
y centra los canales con las medias ImageNet. No se aplica doble normalización.
Los descriptores manuales no se concatenan automáticamente a la red.

Se propone volteo horizontal únicamente en entrenamiento, pendiente de revisión
visual. La extracción profunda con ResNet50 congelado está disponible, pero su
llamada permanece desactivada. Las funciones futuras de entrenamiento comprueban
los reportes y hashes; las incidencias históricas actuales impiden iniciar el ajuste.
Esta condición no sustituye la revisión de identidad por fruto/lote.

## 8. Validación realizada

| Comprobación | Resultado |
|---|---|
| Formato Jupyter y sintaxis | Los cuatro notebooks pasan `nbformat.validate`; todas las celdas Python y los scripts compilan. |
| Ejecución sin dataset | FE, bitácora y preparación ResNet50 terminan sin entrenamiento ni resultados ficticios. |
| Ejecutor del EDA sin dataset | Informa el problema y no cambia el notebook histórico. |
| FE con TIFF temporales | Ejecución completa sobre ocho imágenes técnicas de train; tabla de 77 columnas, incluidos identificadores/configuración; valores finitos y preprocesamiento equivalente al oficial. |
| EDA reubicado | Ejecución en una copia temporal con 18 TIFF; detecta los dos pares duplicados y la contradicción de etiqueta introducidos para la prueba. |
| Integridad de imágenes | Los 18 archivos temporales conservan nombres, particiones y SHA-256 después de ejecutar EDA y FE. |
| Descriptores | Histogramas normalizados; HSV acromático finito; GLCM contrastada con un patrón de resultado conocido; máscara de relleno verificada. |
| Rutas | Detección desde raíz y subcarpetas; rechazo de rutas manuales absolutas Windows/POSIX. |
| ResNet50 | Construcción y un paso de inferencia técnica con pesos ImageNet, extractor congelado de 2048 valores y preprocesamiento correcto. Sin `fit` ni aprendizaje. |
| Conservación | Los 11 archivos originales tienen destino; cinco reportes y salidas del EDA preservados; sin MobileNet ejecutable. |

Los TIFF técnicos, las tablas obtenidas con ellos y sus figuras se utilizaron solo
para comprobar el código. **No forman parte de la entrega ni representan resultados
de clasificación de palta.** Para la comprobación aislada de ResNet50 se cargaron
pesos ImageNet; no se incluyen esos pesos y su descarga no ocurre al ejecutar todas
las celdas de los notebooks entregados con su configuración inicial.

Entorno de prueba: Python 3.12.14, NumPy 2.3.5, pandas 2.2.3, Matplotlib 3.10.8,
Pillow 12.3.0, nbformat 5.11.1, nbclient 0.11.0, ipykernel 7.4.0, IPython 9.17.1,
jupyter_client 8.10.0, TensorFlow CPU 2.21.0, Keras 3.15.1 y scikit-learn 1.8.0.
Los rangos de requirements permiten al instalador resolver una combinación compatible;
las versiones históricas del EDA se mantienen en su JSON original.

## 9. Pendientes para la ejecución local

1. Abrir el proyecto junto a su `DATASET_PALTA` original y seleccionar el kernel.
2. Ejecutar FE para obtener tablas y figuras sobre las imágenes reales.
3. Revisar detalle de defectos, relleno, fondo y pertinencia del volteo horizontal.
4. Resolver en una etapa posterior las incidencias de duplicados/etiquetas y documentar
   independencia por fruto/lote antes de entrenar.

No se dispone de métricas nuevas del dataset real, embeddings exportados de esas
imágenes ni un modelo entrenado. El EDA histórico está conservado y el avance de
Feature Engineering queda implementado para su ejecución local.

### Referencias de implementación

- [Keras: ResNet models](https://keras.io/api/applications/resnet/resnet_models/).
- [TensorFlow: resnet.preprocess_input](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet/preprocess_input).
- [scikit-image: características GLCM](https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_glcm.html).
