import tkinter as tk
from sense_hat import SenseHat

# Instanciamos el SenseHat
sense = SenseHat()

# Creamos el botón de encendido
def limpiar():
    sense.clear()
    print("Pantalla limpiada")

angle = 0
def rotar():
    global angle
    angle += 90
    angle = angle % 360
    sense.set_rotation(angle)
    print("Rotación de la pantalla")	
    
def imprimir():
    sense.show_letter(caja_texto.get()[0])

def salir():
    exit()
    
# Creamos la ventana principal 
ventana = tk.Tk()
ventana.geometry("300x200")
ventana.title("Control de pantalla")

# Botón de limpiar
boton_encender = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_encender.place(x=50, y=50)
# Botón de rotar
boton_apagar = tk.Button(ventana, text="Rotar", command=rotar)
boton_apagar.place(x=150, y=50)
# Creamos un botón para imprimir el mensaje
boton_imprimir = tk.Button(ventana, text="Imprimir", command=imprimir)
boton_imprimir.place(x=100, y=100)
# Creamos un botón peuqeño para salir
boton_salir= tk.Button(ventana, text="X", command=salir, bg="red", fg="white")
boton_salir.place(x=260, y=5)

# Creamos la caja de texto
caja_texto = tk.Entry(ventana)
caja_texto.place(x=50, y=150)
caja_texto.insert(0, "Escribe aquí")

# Bucle principal
ventana.mainloop()