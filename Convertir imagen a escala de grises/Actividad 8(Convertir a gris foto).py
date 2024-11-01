import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

fila = int(2448)
columna = int(3264)

imag = Image.open('tom.jpg')
colores = np.array(imag)

grises = np.zeros((fila, columna))# Inicializar la matriz de grises

for i in range(fila):# Convertir a escala de grises
    for j in range(columna):
        grises[i][j] = colores[i][j][0] * 0.2989 + colores[i][j][1] * 0.5870 + colores[i][j][2] * 0.1140
    print("Cargando...")

plt.imshow(grises, cmap='gray')
plt.show()
