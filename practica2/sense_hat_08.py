import random
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time

O = [255, 0, 0]  # Rojo
X = [255, 255, 255]  # Blanco 

UNO = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

DOS = [
    X, X, O, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, X, X
]

TRES = [
    X, X, O, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, X, X,
    O, O, O, O, O, O, X, X
]

CUATRO = [
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X
]

CINCO = [
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, O, O, O, O,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X
]

SEIS = [
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
    O, O, O, O, O, O, O, O,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
    O, O, O, O, O, O, O, O,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X
]

numeros = [UNO, DOS, TRES, CUATRO, CINCO, SEIS]

def dado_loco():
    # Esperamos a que se suelte el joystick
    sense.stick.wait_for_event(ACTION_PRESSED)
    while True:
        # Encender todos los leds
        sense.set_pixels(random.choice(numeros))
        # Esperar 0.1 segundos
        time.sleep(0.1)
        # Salir del ciclo si se suelta el joystick
        if sense.stick.wait_for_event().action == ACTION_RELEASED:
            return
        

# Crear una instancia de la clase SenseHat
sense = SenseHat()

# Limpiar la matriz de leds
sense.clear()

while True:
    # Cambiamos muy rapido los numeros 
    # del dado hasta pulsar el joystick
    dado_loco()
    # Seleccionar un numero aleatorio
    numero = random.choice(numeros)
    # Mostrar el numero en la matriz de leds
    sense.set_pixels(numero)
    
    