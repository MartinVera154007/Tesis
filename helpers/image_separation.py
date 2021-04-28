### Script para separar la imagenes del dataset AVA ###
import shutil
import os

# Ruta donde se alamacenan las imagenes
ruta_imagenes = r'C:\Users\veram\Desktop\Escuela\Seminario\AVA_dataset\images\images'

# Ubicar y abrir el archivo con los nombres de las imagenes
ruta_archivo_imagenes = r'C:\Users\veram\Desktop\Escuela\Seminario\AVA_dataset\style_image_lists\train_images.txt'
archivo_imagenes = open(ruta_archivo_imagenes)
lineas = archivo_imagenes.read().splitlines()

# Ubicar y abrir el archivo con las etiquetas de las imagenes
ruta_archivo_etiquetas = r'C:\Users\veram\Desktop\Escuela\Seminario\AVA_dataset\style_image_lists\train_labels.txt'
archivo_etiquetas = open(ruta_archivo_etiquetas)

# Recorrer el archivo de imagenes y copiarlas en su carpeta correspondiente
for linea in lineas:
    nombre_imagen = linea.strip()
    etiqueta_imagen = archivo_etiquetas.readline().strip()
    archivo_origen = ruta_imagenes + '\\' + nombre_imagen + '.jpg'
    ruta_destino = ruta_imagenes + '\\' + etiqueta_imagen
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)
    shutil.copy(archivo_origen, ruta_destino)

archivo_imagenes.close() 
archivo_etiquetas.close()
print('-----Ejecucion Finalizada-----')