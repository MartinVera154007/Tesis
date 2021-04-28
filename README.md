# Proyecto de titulación
Red Neuronal Convolucional Para la Clasificación de Estilos Fotográficos

## Descripción
Proyecto en el que se implementó una red neuronal para la clasificar 14 estilos fotográficos. El dataset utilizado (AVA) se puede obtener de https://github.com/mtobeiyf/ava_downloader. 

Los subconjuntos de AVA utilizados para este proyecto son:
 * ava (11,253 imágenes): conjunto de imágenes separadas por estilo y en los sets de train, test y valid. https://drive.google.com/file/d/1CiMlIl6SikzJZigeBa3RjDSq3sTilQ8z/view?usp=sharing
 * ava_augmented_full (33,759 imágenes): similar a ava, pero con aumento de datos (proyección horizontal y vertical de cada imagen). https://drive.google.com/file/d/1-3b42pNKVMP6d2fQKcvNyBw4j7Wz0TH8/view?usp=sharing
 * ava_augmented_balanced (14,656 imágenes): similar al anterior, pero el aumento solo fue realizado de tal manera que las clases que tuvieran menos de 1000 muestras alcanzaran dicha cifra. https://drive.google.com/file/d/1HR4VQ-CIeEr_hHc04k1f5zD2DxAoftzc/view?usp=sharing

## Carpeta helpers
Esta carpeta contiene algunos scripts que fueron utilizados antes o después del entrenamiento de los modelos.

* image_separation: Separa las imágenes por estilos del dataset AVA.
* image_split: Hace el split en train, test y valid. Se tiene que tener el dataset separado por clases. 
* Augment Images: Aumenta las imágenes del dataset haciendoles una proyección sobre el eje horizontal y vertical a cada imagen.
* Augment Images to Get Balance: Similar al anterior pero en este caso solo se hace el aumento en aquellas clases que contengan menos de 1000 imágenes para alcanzar dicha cifra.
* Model testing: Se utiliza para probar modelos ya entrenados y calcular las métricas necesarias.
* Interface: Interfaz de consola para probar una modelo ya entrenado. Revise como entrada una imagen y devuelve como salida el estilo de la imagen.

Los scripts "image_separation" e "image_split" fueron ejecutados localmente utilizando el dataset completo de AVA con el fin de extraer el subconjunto que serviría para la clasificación de estilos. Una vez obtenido dicho subconjunto, se subió a Google Drive, y el resto del proyecto fue trabajado completamente en la nube.

## Carpeta modelos_entrenamiento
Esta carpeta contiene el entrenamiento de los modelos utilizados en el proyecto. A continuación se describe la nomnenclatura utilizada en el nombre de los notebooks para identificar de mejor manera a que modelo corresponde cada uno:
* Primero se comienza con el nombre del modelo.
* La palabra "dropout" indica que el modelo fue modificado para agregarle algunas capas extras de dropout. De no tenerla, se utilizó el modelo tal cual.
* La palabra "Imagenet" indica que el modelo utilizó los pesos aprendidos del dataset Imagenet, es decir, utilizó transfer learning. De no tenerla, el modelo fue entrenado desde cero.
* La palabra "completamente" indica que el modelo fue entrenado con el dataset completamente aumentado. De no tenerla, se utilizo el dataset sin aumentar.
* La palabra "balanceado" indica que el modelo fue entrenado con el dataset balanceado. De no tenerla, se utilizo el dataset sin aumentar.
* Aquellos modelos que no indiquen un número de clases fueron entrenados para clasificar las 14 clases del dataset AVA.

## Nota
**Todos los modelos fueron creados y entrenados utilizando el entorno en la nube de Google Colab. Por esta razón podrá encontrar algunos comandos de terminal Linux que son utilizados para cargar los datos a las sesiones del servicio Colab, y/o guardar datos nuevos creados en Google Drive. En caso de que se quieran replicar los experimentos aquí presentados en un entorno diferente considere hacer los ajustes necesarios.**
