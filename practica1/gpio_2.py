from gpiozero import DigitalOutputDevice, DigitalInputDevice
from signal import pause
import time

# Configuramos el dispositivo de salida digital (LED) en el pin GPIO 1
led = DigitalOutputDevice(1)

# Configuramos el dispositivo de entrada digital (Botón) en el pin GPIO 2
button = DigitalInputDevice(2)

# Definimos la función que manejará la interrupción (cambiar el LED)
def manejar_led():
    
    if led.value == 1:
        led.off()
        print("El LED está apagado")
    else:
        led.on()
        print("El LED está encendido")

# Detectamos cuando el botón es presionado
button.when_activated = manejar_led

# Mantener el script corriendo
while True:
    
    # En este punto, el programa puede hacer otras cosas
    # porque la interrupción se encargará de encender el LED
    
    time.sleep(2) 
    print("Otros cálculos ...")
    for i in range(10):
        print(i)
        time.sleep(0.5)
