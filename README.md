# Proyecto de titulación
Red Neuronal Convolucional Para la Clasificación de Estilos Fotográficos

## Carpeta helpers
Esta carpeta contiene algunos scripts que fueron utilizados antes o después del entrenamiento de los modelos.

* image_separation: Separa las imágenes por estilos del dataset AVA.
* image_split: Hace el split en train, test y valid. Se tiene que tener el dataset separado por clases. 
* Augment Images: Aumenta las imágenes del dataset haciendoles una proyección sobre el eje horizontal y vertical a cada imagen.
* Augment Images to Get Balance: Similar al anterior pero en este caso solo se hace el aumento en aquellas clases que contengan menos de 1000 imágenes para alcanzar dicha cifra.
* Model testing: Se utiliza para probar modelos ya entrenados y sacar las métricas necesarias.
* Interface: Interfaz de consola para probar una modelo ya entrenado. Revise como entrada una imagen y devuelve como salida el estilo de la imagen.
