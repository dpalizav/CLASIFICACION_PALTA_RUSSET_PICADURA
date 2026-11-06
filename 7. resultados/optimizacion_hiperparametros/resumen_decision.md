# Resultados de optimización de hiperparámetros

Modelo: ResNet50 ImageNet con ajuste fino del bloque conv5, cabeza D1 y fotometria train.
Metrica central: Macro-F1 sobre VALIDATION. TEST no utilizado.
Metodo: Optuna RandomSampler, semilla 42; 8 ensayos completados de 8 previstos.
Rango de learning rate (log): 3e-06 a 3e-05.
Rango de dropout: 0.25 a 0.45.
Presupuesto de entrenamiento: hasta 8 epocas, lote 1, early stopping por val_loss.

Mejor ensayo: 0.
Learning rate: 1e-05; dropout: 0.3500.
Macro-F1 de validation: 0.7876.
Recall RUSSET: 0.7143.
Macro-F1 historico FT_D1_PHOTO: 0.7876 (solo antecedente; no sustituye la referencia interna).
Macro-F1 referencia interna, trial 0: 0.7876
Diferencia frente al trial 0: +0.0000

Decision: configuracion candidata preliminar; no se adopta automaticamente por una mejora puntual en validation.
Verificar estabilidad con repeticiones independientes, tradeoffs por clase y costo antes de adoptarla.
No se calcularon media ni desviacion estandar entre semillas: una corrida por configuracion.
Un ajuste de hiperparametros en esta misma particion puede optimizarse al ruido de validation.
Estos ensayos no incluyen una nueva evaluacion independiente sobre TEST ni resultados de despliegue industrial.
