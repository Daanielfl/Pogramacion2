def CifradoCesar(text, desp):
    NumToLetter = ""
    
    for i in text:
        
        if i.isalpha(): # Sirve para solo cifrar letras, que el usuario no agreue ningun caracter ni nada por el estilo
            
            if i.isupper(): # Acá determinamos el rango entre mayusculas y minusculas
                base = ord('A')
            else:
                base = ord('a')

            
            num = (ord(i) - base + desp) % 26 + base # Aplicar el desplazamiento y volvemos al númer base, al inicio ("A"-"a")
            NumToLetter += chr(num)
        else:
            
            NumToLetter += i # A un  signo o a un número, lo agrega sin cambios
            
    return NumToLetter

fin = ""
none = ""
cars = 0

while True: # While sin terminar para que el usuario termine cuando lo desee él.
    none = input("Ingrese la palabra que desea cifrar: ")
    cars = int(input("Ingrese la cantidad de desplazamiento que desea hacer: "))
    na = CifradoCesar(none, cars)
    print(na)
    fin = input("Ingrese Si para terminar: ")

    if fin == "si" or fin == "Si":
        break

