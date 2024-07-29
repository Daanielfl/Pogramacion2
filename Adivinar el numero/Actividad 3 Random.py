# importó el modulo random
import random

# decleró las variables
min = 1
max = 20
y = random.randint(min,max)
x = 0
i = 0
life = 6

print(f"El número se encuentra entre {min} y {max}")

# comparó el númeo del usuario 
while life > i:
    # ingesa un número el usuario 
    x = int(input("Adivine el número secreto "))
    i = i + 1
    # comparo el número del usuario 
    if x < y:
        print("Su número es menor al número secreto")
    elif x > y:
        print("Su número es mayor al número secreto")
    elif x == y:
        print(f"Muy bien usted a adivinado el número secreto lo logró en {i} intento/s el número fue {y}")
        break
if life == i:
    print(f"Ya usó sus {life} intentos :( y no adivinó el número, el número era {y}")
    
    