# Resultados de entrenamiento

Se completaron B0 y V1 con ResNet50 ImageNet congelada y cabeza Dropout + Dense. Las características deterministas se calcularon una vez en memoria; la cabeza se entrenó realmente durante 15 épocas y se seleccionó la época 8 por val_loss en ambas condiciones. Las predicciones finales se obtuvieron con el modelo compuesto completo.

| Condición | Accuracy | Macro-F1 | Balanced accuracy | Recall RUSSET |
|---|---:|---:|---:|---:|
| B0 | 0.842520 | 0.660428 | 0.638365 | 0.333333 |
| V1 | 0.858268 | 0.659821 | 0.628706 | 0.285714 |
| V2 | No ejecutada | No ejecutada | No ejecutada | No ejecutada |

V2 está bloqueada porque el responsable confirmó que debe conservarse el orden horizontal de las capturas. No se reemplazó por otra transformación.

Se verificaron los 829 archivos y se excluyeron lógicamente los cuatro implicados en los dos pares duplicados: 572 train, 127 validation y 126 test reservado. No se evaluó test. Los hashes no garantizan independencia por fruto/lote.

Las carpetas B0_s42_01 y V1_s42_01 contienen configuración, auditoría, listas elegibles, historia, métricas, predicciones y gráficos reales. Los pesos de la cabeza y la caché ImageNet permanecen locales y excluidos de Git. Repetir desde resnet50.ipynb con otro identificador, el mismo protocolo y el entorno palta. Los tiempos se midieron con 8 hilos intra-op y 2 inter-op, en procesos separados.

El README raíz conserva cambios previos del usuario y describe la etapa anterior. Este documento y el informe registran el estado experimental actual.

El PDF fue renderizado e inspeccionado. El DOCX se validó estructuralmente; su render nativo quedó pendiente por falta de LibreOffice y bloqueo de automatización Word. Ambos contienen el mismo informe, con posible diferencia de paginación.
