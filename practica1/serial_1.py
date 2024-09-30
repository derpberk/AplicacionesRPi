import serial
import gpiozero

# Configuramos el puerto serie
TTY = '/dev/ttyACM0'  # usb
BAUDRATE = 9600
# Creamos la comunicación: 1 bit de stop, sin paridad
puerto_serie = serial.Serial(TTY, BAUDRATE)

# Configuración del pin GPIO1
led = gpiozero.DigitalOutputDevice("GPIO1")

while True:
    
    if puerto_serie.in_waiting > 0:
        # Leemos un byte
        data = puerto_serie.read(1).decode()
        puerto_serie.write(data.encode())
        print("Recibido: ", data)
        
        # Encendemos o apagamos el led
        if data == '1':
            led.on()
        elif data == '0':
            led.off()
        else:
            print("Mensaje no válido")
            
