import gpiozero
import time

# Creamos el objeto DigitalOutputDevice
led = gpiozero.DigitalOutputDevice(1)
# Creamos el objeto DigitalInputDevice
button = gpiozero.DigitalInputDevice(2, pull_up=True, bounce_time=0.1)

while True:
    # Leemos el valor del botón
    estado_boton = button.value
    
    # Solo si el botón está pulsado
    if estado_boton.value == 1:
        
        # Cambiamos el estado del led al contrario del actual
        if led.value == 1: # Si el led está encendido
            led.off()
        else: # Si el led está apagado
            led.on()
    
    