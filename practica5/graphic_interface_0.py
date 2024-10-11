import tkinter as tk
from sense_hat import SenseHat

# Instanciamos el SenseHat
sense = SenseHat()

# Creamos el botón de encendido
def limpiar():
    sense.clear()
    print("Encendido")

angle = 0
def rotar():
    angle += 90
    angle = angle % 360
    sense.set_rotation(angle)
    print("Apagado")
    
def imprimir():
    sense.show_letter(caja_texto.get()[0])
    print(caja_texto.get())
    
# Creamos la ventana principal 
ventana = tk.Tk()
ventana.geometry("300x200")
ventana.title("Control de pantalla")

# Creamos los botones
boton_encender = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_encender.place(x=50, y=50)
boton_apagar = tk.Button(ventana, text="Rotar", command=rotar)
boton_apagar.place(x=150, y=50)

# Creamos un botón para imprimir el mensaje
boton_imprimir = tk.Button(ventana, text="Imprimir", command=imprimir)
boton_imprimir.place(x=100, y=100)

# Creamos un botón peuqeñopara salir
boton_salir= tk.Button(ventana, text="X", command=exit(), bg="red", fg="white")
boton_salir.place(x=5, y=100)

# Creamos la caja de texto
caja_texto = tk.Entry(ventana)
caja_texto.place(x=50, y=150)
caja_texto.insert(0, "Escribe aquí")

# Bucle principal
ventana.mainloop()