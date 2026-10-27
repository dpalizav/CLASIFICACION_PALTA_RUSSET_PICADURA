# Registro de cambios

Se conservo la organizacion original del proyecto y los resultados de EDA, Feature Engineering, B0 y V1.

## Notebooks

- Se mantuvieron `4. EDA/01_EDA.ipynb` y `5. feature_engineering/feature_engineering_palta.ipynb`, con el mismo codigo y las mismas salidas. Se simplifico el formato de sus celdas Markdown.
- Se mantuvo la bitacora de `1. fuentes/` y se retiraron las negritas de su Markdown.
- Se amplio `6. entrenamiento/resnet50.ipynb` con D1 y D2. Generan copias fotometricas de RUSSET en memoria. No separan las 30 vistas ni cambian los TIFF.
- Se anadio una comprobacion de GPU y una funcion opcional para fine-tuning parcial del bloque conv5.
- `2. informe/Informe.ipynb` reemplaza los documentos PDF y Word del informe. Sus tablas y graficos leen los resultados guardados.

## Balanceo propuesto

La lista elegible de train registra 495 PICADURA y 77 RUSSET.

- B0: 495 PICADURA y 77 RUSSET.
- D1: 495 PICADURA, 77 RUSSET originales y 77 copias.
- D2: 495 PICADURA, 77 RUSSET originales y 154 copias.

Cada copia tiene un registro CSV con archivo de origen, numero de copia y factores de brillo/contraste. Los pesos de clase se calculan con los conteos de cada corrida. Las copias no son frutos nuevos.

## Ejecucion

B0 y V1 ya tienen metricas reales. D1, D2 y fine-tuning no se han ejecutado en esta entrega porque el dataset TIFF esta en la computadora local, no en el archivo comprimido.

Las corridas nuevas se ejecutan una por vez, tras verificar la auditoria de integridad y aprobar las exclusiones. Test permanece reservado para la evaluacion final. No se genero ni subio ningun TIFF sintetico.

El paquete no incluye PDF ni DOCX. No se modifico ningun repositorio remoto.
