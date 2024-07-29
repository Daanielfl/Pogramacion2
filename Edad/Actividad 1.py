Nombre = ""
AñoNaci = 0
AñoAct = 0

Nombre = input("Me dice su nombre: ")

print("Hola "+Nombre+" podría decirme en que año estamos")
AñoAct = int(input())

AñoNaci= int(input("Ah okey, y usted en que año nacío?: "))

Edad = AñoAct - AñoNaci

print("Usted tiene ",Edad," Años")


