import random

# Declaro las variables
dificultad = 0

# Selección de dificultad
while dificultad != 1 and dificultad != 2:
    dificultad = int(input("Seleccione la dificultad 1 para Fácil y 2 para Difícil: "))
    if dificultad == 1 or dificultad == 2:
        break

def ComparoNumero(y, life):
    i = 0
    # Comparo el número del usuario
    while life > i:
        # Ingresa un número el usuario 
        x = int(input("Adivine el número secreto: "))
        i += 1
        # Comparo el número del usuario 
        if x < y:
            print("Su número es menor al número secreto")
        elif x > y:
            print("Su número es mayor al número secreto")
        elif x == y:
            print(f"Muy bien, usted ha adivinado el número secreto. Lo logró en {i} intento(s). El número fue {y}.")
            break
    if life == i:
        print(f"Ya usó sus {life} intentos :( y no adivinó el número. El número era {y}.")

# Selección de la dificultad
if dificultad == 1:
    min = 1
    max = 20
    life = 6
elif dificultad == 2:
    min = 1
    max = 200
    life = 7

# Genero el número secreto
y = random.randint(min, max)

# Llamo a la función
ComparoNumero(y, life)

