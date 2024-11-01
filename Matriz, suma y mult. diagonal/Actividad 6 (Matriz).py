# Actividad 6) Declarar una matriz de 4 cifras y 4 columnas co números sucesivos en cada celda. Calcular la suma y la
# multiplicación de la diagonal principaly de la contra diagonal. Mostrar en pantalla estos valores y los elementos
# de la matriz
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Variables
speed = 0
monster = 1
clp = 0
alt = 1

# Matriz
Fo=[[1, 2, 3, 4,],
        [5 , 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

# Recorro la matriz
for a in range(len(Fo)):
    for x in range(len(Fo)):

# Para sumar solo las diagonales        
        if a==x:
            speed = speed + Fo[a][x]
            monster = monster * Fo[a][x]
            print(Fo[a][x])
            
        if x==len(Fo)-1-a:
            clp = clp + Fo[a][x]
            alt = alt * Fo[a][x]


print("La suma es ", speed)
print("La multiplicación es ", monster)
print('-------------------------------------------')
print("La contra suma es ",clp)
print("La contra multiplicación es ",alt)