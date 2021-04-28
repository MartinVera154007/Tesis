# Script tomar una muestar de las imagaenes ya SEPARADAS por clases (una carpeta por clase) del dataset AVA 
# Este script modifical el dataset (el directorio y su contenido) original
import shutil
import os
import random
import glob

# Ruta donde se alamacenan las imagenes
ruta_imagenes = r'C:\Users\veram\Desktop\Escuela\Seminario\wikiart\wikiart\wikiart' # Ruta del dataset COMPLETO y SEPARADO por clases
porcentaje_imagenes = 1.00 # Porcentaje del TOTAL de imagenes con el que se va a trabajar
porcentaje_train = 0.80 # Porcentaje para el set de entranamiento
porcentaje_test = 0.10 # Porcentaje para el set de prueba
procentaje_valid = 0.10 # Porcentaje para el set de validacion

# Crear los directorios de Train, Test y Valid
ruta_train = ruta_imagenes + '\\' + 'train'
ruta_test = ruta_imagenes + '\\' + 'test'
ruta_valid = ruta_imagenes + '\\' + 'valid'
os.makedirs(ruta_train, exist_ok = True)
os.makedirs(ruta_test, exist_ok = True)
os.makedirs(ruta_valid, exist_ok = True)

# Obtener la lista de carpetas en el directorio del dataset
directorios = os.listdir(ruta_imagenes)

# Remover de la lista los directorios que se acaban de crear
directorios.remove('test')
directorios.remove('train')
directorios.remove('valid')
print(directorios)

# Recorrer cada directorio (clase) del dataset, tomar las muestras de las imagenes
# y moverlas al directorio correspondiente (train, test y valid)
for directorio in directorios: 
    ruta_directorio = ruta_imagenes + '\\' + directorio
    lista_directorios = os.listdir(ruta_directorio)
    total_archivos = len(lista_directorios)

    # Obtener la cantidad de imagenes segun los porcentajes seleccionados
    imagenes_requeridas = int(total_archivos * porcentaje_imagenes)
    cantidad_train = int(imagenes_requeridas * porcentaje_train)
    cantidad_test = int(imagenes_requeridas * porcentaje_test)
    cantidad_valid = int(imagenes_requeridas * procentaje_valid)
 
    # Mover la imagenes correspondientes al set de entrenamiento
    ruta_train_actual = ruta_train + '\\' + directorio
    os.makedirs(ruta_train_actual, exist_ok = True)
    for imagen in random.sample(glob.glob(ruta_directorio + '/*'), cantidad_train):
        shutil.move(imagen, ruta_train_actual)
        print('Imagen movida ✔')
    
    # Mover las imagenes correspondientes al set de pruebas
    ruta_test_actual = ruta_test + '\\' + directorio
    os.makedirs(ruta_test_actual, exist_ok = True)
    for imagen in random.sample(glob.glob(ruta_directorio + '/*'), cantidad_test):
        shutil.move(imagen, ruta_test_actual)
        print('Imagen movida ✔')

    # Mover las imagenes correspondientes al set de validacion
    ruta_valid_actual = ruta_valid + '\\' + directorio
    os.makedirs(ruta_valid_actual, exist_ok = True)
    for imagen in random.sample(glob.glob(ruta_directorio + '/*'), cantidad_valid):
        shutil.move(imagen, ruta_valid_actual)
        print('Imagen movida ✔')

print('-----Ejecucion Finalizada-----')