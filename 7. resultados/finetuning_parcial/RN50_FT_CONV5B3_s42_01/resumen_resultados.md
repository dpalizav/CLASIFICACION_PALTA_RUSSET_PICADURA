# Resultados Sprint 11: fine-tuning parcial de ResNet50

La cabeza se entrenó de cero con ResNet50 ImageNet, sin cargar checkpoints históricos. Se modificó únicamente el alcance de fine-tuning a conv5_block3 respecto del Sprint 09.

- VALIDATION (127): Macro-F1=0.8515, precisión RUSSET=0.7083, recall RUSSET=0.8095.
- Backbone ajustable: 7 capas, 4459520 parámetros.

**Alcance:** una semilla, validación pequeña y ya utilizada en el desarrollo. No se calcularon predicciones de 260423 ni TEST. La comparación es exploratoria; no demuestra una mejora generalizable.
