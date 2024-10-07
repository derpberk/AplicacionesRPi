import gpiozero
import time

# Creamos el objeto DigitalOutputDevice
led = gpiozero.DigitalOutputDevice(1)

while True:
	time.sleep(0.5)  # Espera 0.5 segundos
	led.on()  # Ponemos el pin a valor ALTO (3.3V)
	time.sleep(0.5)  # Espera 0.5 segundos
	led.off() # Ponemos el pin a valor BAJO (0V)
