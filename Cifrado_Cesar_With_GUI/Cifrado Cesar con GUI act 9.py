import tkinter as tk

# Ventana principal
gui = tk.Tk()
gui.geometry("400x500")
gui.configure(background="gray")
tk.Wm.wm_title(gui, "Cifrado César")

text = tk.StringVar(gui)
desp = tk.IntVar(gui)

# Función para cifrar el texto

def CifradoCesar():
    # Usamos text.get para llamar loa funcion que esta fuera
    input_text = text.get()
    desplazamiento = desp.get()  
    NumToLetter = ""
    
    # Recorrer cada carácter del texto
    for i in input_text:
        if i.isalpha():  # Si es una letra
            if i.isupper():  # Si es mayúscula
                base = ord('A')  # Base de las mayúsculas
            else:
                base = ord('a')  # Base de las minúsculas

            # Aplicar el desplazamiento en el alfabeto
            num = (ord(i) - base + desplazamiento) % 26 + base
            NumToLetter += chr(num)  # Añadir la letra cifrada al resultado
        else:
            NumToLetter += i  # Si no es letra, agregar el carácter tal cual
    
    
    result_label.config(text=f"Texto Cifrado: {NumToLetter}")

# Etiqueta para ingresar el texto a cifrar

tk.Label(
    gui,
    text="¿Qué palabra desea cifrar?",
    font=("Verdana", 15),
    fg="white",
    bg="light blue",
    justify="left",
).pack(fill=tk.BOTH, expand=True)

# Entrada de texto para que el usuario ingrese el texto a cifrar

text_entry = tk.Entry(
    gui,
    fg="white",
    bg="brown",
    justify="left",
    textvariable=text,
).pack(fill=tk.BOTH, expand=True)

# Etiqueta para ingresar el desplazamiento

tk.Label(
    gui,
    text="Ingrese el desplazamiento",
    font=("Verdana", 15),
    fg="black",
    bg="light green",
    justify="left",
).pack(
    fill=tk.BOTH,
    expand=True
    )

# Entrada para que el usuario ingrese el desplazamiento

desp_entry = tk.Entry(
    gui,
    fg="white",
    bg="brown",
    justify="left",
    textvariable=desp,
).pack(
    fill=tk.BOTH,
    expand=True
    )

# Botón para realizar el cifrado

tk.Button(
    gui,
    text="Cifrar",
    font=("Verdana", 16),
    bg="light green",
    fg="black",
    command=CifradoCesar,
    justify="center",
).pack(fill=tk.BOTH, expand=True)

# Muestra el texto cifrado

result_label = tk.Label(
    gui,
    text="Texto Cifrado: ",
    font=("Verdana", 15),
    fg="white",
    bg="light blue",
    justify="left",
)
result_label.pack(
    fill=tk.BOTH,
    expand=True
    )

gui.mainloop()