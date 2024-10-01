import tkinter as tk
import gpiozero
from sense_hat import SenseHat

# Creamos el objeto LED
led = gpiozero.DigitalOutputDevice("GPIO1")

# Instanciamos el SenseHat
sense = SenseHat()

# Creamos el botón de encendido
def encender():
    led.on()
    print("Encendido")

def apagar():
    led.off()
    print("Apagado")
    
def imprimir():
    sense.show_message(caja_texto.get())
    print(caja_texto.get())
    
# Creamos la ventana principal 
ventana = tk.Tk()
ventana.geometry("300x200")
ventana.title("Control de LED")

# Creamos los botones
boton_encender = tk.Button(ventana, text="Encender", command=encender)
boton_encender.place(x=50, y=50)
boton_apagar = tk.Button(ventana, text="Apagar", command=apagar)
boton_apagar.place(x=150, y=50)

# Creamos un botón para imprimir el mensaje
boton_imprimir = tk.Button(ventana, text="Imprimir", command=imprimir)
boton_imprimir.place(x=100, y=100)

# Creamos la caja de texto
caja_texto = tk.Entry(ventana)
caja_texto.place(x=50, y=150)
caja_texto.insert(0, "Escribe aquí")

# Bucle principal
ventana.mainloop()