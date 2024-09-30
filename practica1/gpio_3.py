from gpiozero import PWMOutputDevice
from time import sleep
from signal import pause

# Configuramos el dispositivo de salida PWM (LED) en el pin GPIO 1
led = PWMOutputDevice(1, active_high=True, initial_value=0, frequency=1000)

# Definimos una función para cambiar la intensidad del LED
def ajustar_intensidad():
    # Ajustamos el ciclo de trabajo a diferentes niveles
    for i in range(0, 101, 10):
        led.value = i / 100.0  # Ajustamos el ciclo de trabajo (0.0 a 1.0)
    print(f"Intensidad del LED: {i}%")
    sleep(1)

# Llamamos a la función para ajustar la intensidad del LED
ajustar_intensidad()

# Mantener el script corriendo
pause()