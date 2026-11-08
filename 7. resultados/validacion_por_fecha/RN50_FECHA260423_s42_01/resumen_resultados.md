# Resultados Sprint 09: validación por fecha

La cabeza se entrenó desde cero sobre ResNet50 ImageNet. No se cargaron checkpoints históricos.

- VALIDATION original (127): Macro-F1=0.7900, recall RUSSET=0.6667.
- Evaluación exploratoria 260423 (43): Macro-F1=0.7081, recall RUSSET=0.9091.

**Interpretación:** la evaluación por fecha es exploratoria; no es un TEST independiente ni debe utilizarse para ajustar la próxima configuración. El dataset histórico y el nuevo TRAIN son diferentes: no atribuir las diferencias únicamente al cambio de validación.
