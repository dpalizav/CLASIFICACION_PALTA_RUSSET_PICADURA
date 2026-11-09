# Resultados Sprint 10: regularización controlada con AdamW

Se entrenó una nueva cabeza desde ImageNet con exactamente los mismos conjuntos, D1, semilla y tasas del Sprint 09. El único cambio es AdamW (weight_decay=0.01) en ambas etapas.

- VALIDATION original (127): Macro-F1=0.7923, recall RUSSET=0.6190, precisión RUSSET=0.6842.

**Limitaciones:** la comparación usa el conjunto de desarrollo ya consultado en los sprints anteriores. La diferencia de una sola semilla no es evidencia estadística de mejora. No se ha consultado 260423 ni TEST en esta corrida.
