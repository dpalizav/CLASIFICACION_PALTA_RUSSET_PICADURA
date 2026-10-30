# Sprint 7. Análisis de importancia de variables visuales

Modelo: FT_D1_PHOTO_s42_01.
Partición utilizada: validation, 127 TIFF completos (106 PICADURA y 21 RUSSET).
No se realizó entrenamiento ni se volvió a evaluar TEST.

## Resultados observados

| Condición | Accuracy | Macro-F1 | Δ Macro-F1 | Cambios de etiqueta |
|:--|--:|--:|--:|--:|
| imagen_completa | 0.8661 | 0.7781 | +0.0000 | 0 |
| camara_1_ocultar | 0.8898 | 0.7354 | +0.0427 | 19 |
| camara_2_ocultar | 0.8583 | 0.7883 | -0.0102 | 11 |
| camara_3_ocultar | 0.6457 | 0.6066 | +0.1714 | 40 |
| camara_1_desenfocar | 0.6929 | 0.6120 | +0.1661 | 26 |
| camara_2_desenfocar | 0.7795 | 0.6945 | +0.0836 | 17 |
| camara_3_desenfocar | 0.5906 | 0.5609 | +0.2172 | 47 |
| brillo_0.95 | 0.8819 | 0.7900 | -0.0120 | 4 |
| brillo_1.05 | 0.8661 | 0.7781 | +0.0000 | 0 |
| contraste_0.95 | 0.8819 | 0.7974 | -0.0194 | 2 |
| contraste_1.05 | 0.8661 | 0.7781 | +0.0000 | 0 |

## Interpretación descriptiva

Entre las ocultaciones, camara_3_ocultar produjo la mayor caída observada de Macro-F1 (+0.1714). Esta relación es de sensibilidad bajo intervención artificial, no causalidad.
La mayor variación absoluta del Macro-F1 entre los cambios fotométricos se observó en contraste_0.95 (Δ=-0.0194).
La reproducción de validation difirió del registro histórico en 1 etiquetas y su diferencia máxima de probabilidad fue 0.004967; no se considera una reproducción exacta si hay discordancias.

## Limitaciones

El conjunto validation es limitado y presenta desbalance. La ocultación/desenfoque introduce imágenes modificadas, que pueden quedar fuera de la distribución original. Las estimaciones no equivalen a importancia causal ni prueban robustez industrial.
La evaluación TEST permanece cerrada desde el corte anterior.

## Evidencia generada

- importancia_camaras_validation.csv
- sensibilidad_fotometrica_validation.csv
- resumen_importancia_validation.csv
- protocolo_importancia.json
- importancia_camaras_validation.png
- sensibilidad_fotometrica_validation.png
- gradcam_ejemplos_validation.png (solo si se activa Grad-CAM)
