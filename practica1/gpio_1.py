import gpiozero
import time

# Creamos el objeto DigitalOutputDevice
led = gpiozero.DigitalOutputDevice(1)
# Creamos el objeto DigitalInputDevice
button = gpiozero.DigitalInputDevice(2, pull_up=True, bounce_time=0.1)

estado_boton_actual = 0
estado_boton_anterior = 0

while True:
    # Leemos el valor del botón
    estado_boton_actual = button.value
    
    # Solo si el botón está pulsado
    if estado_boton_actual == 1 and estado_boton_anterior == 0:
        
        # Cambiamos el estado del led al contrario del actual
        if led.value == 1: # Si el led está encendido
            led.off()
        else: # Si el led está apagado
            led.on()
            
    # Guardamos el estado actual del botón para la siguiente iteración
    estado_boton_anterior = estado_boton_actual
    
    