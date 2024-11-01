import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
plt.rcParams['image.cmap'] = 'gray'

from PIL import Image, ImageOps

int1 = Image.open('tom.jpg')
intlgr = ImageOps.grayscale(int1)
Foto = np.array(intlgr)

ax       = 0
fila     = 2448
columna  = 3264
io       = columna - 1 

for i in range(fila):
    for z in range(int(columna/2)):
        ax = Foto[i][z]
        Foto[i][z] = Foto[i][io-z]
        Foto[i][io-z] = ax
        
plt.imshow(Foto)
plt.show()