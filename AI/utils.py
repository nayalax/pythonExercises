# Preprocesamiento de imágenes
from keras.models import load_model
import numpy as np
from PIL import Image


def cargar_y_preprocesar_imagen(ruta_imagen, tamano=(64, 64)):
# Cargar la imagen
    imagen = Image.open(ruta_imagen).convert('RGB')
    imagen = imagen.resize(tamano)
    imagen = np.array(imagen)
    imagen = imagen / 255.0 # Normalización
    return imagen
    
def predecir_imagen(ruta_imagen):
    modelo = load_model('modelo_cats_vs_dogs.keras')
    imagen = cargar_y_preprocesar_imagen(ruta_imagen)
    imagen = np.expand_dims(imagen, axis=0)
    prediccion = modelo.predict(imagen)
    if prediccion[0][0] > 0.5:
        print("Es un perro")
    else:
        print("Es un gato")