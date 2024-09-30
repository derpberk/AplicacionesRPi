import serial
import time

TTY = '/dev/ttyS0'
BAUDRATE = 9600
# Creamos la comunicación: 1 bit de stop, sin paridad
uart = serial.Serial(TTY, BAUDRATE)

# Enviamos un mensaje inicial
mensaje = "Hello from Raspberry Pi!\n"
uart.write(mensaje.encode())
time.sleep(1)

while True:
    
    if uart.in_waiting > 0:
        # Leemos el mensaje cuando haya algo en el buffer
        data = uart.read(uart.in_waiting).decode()
        print(data)
        
        # Enviamos un mensaje de vuelta
        uart.write(mensaje.encode())
        time.sleep(1)
