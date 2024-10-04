from picamera2 import Picamera2
import gpiozero
from time import sleep


# Creamos un objeto tipo Button 
button = gpiozero.Button("GPIO1", pull_up=False)

# Instanciamos la clase PiCamera2
camera = PiCamera2()
# Configuramos la resolución y rotación de la cámara
camera.resolution = (640,480)
camera.rotation = 180
# Iniciamos la vista previa de la cámara

index = 0

while True:
    
    # Usamos el método wait_for_press() 
    # para esperar a que el botón sea presionado
    button.wait_for_press() 
    # Iniciamos la vista previa de la cámara
    camera.start_preview(fullscreen=False, window=(30,30,320,240)) 
    sleep(5) # Esperamos 5 segundos
    camera.stop_preview() # Detenemos la vista previa
    camera.capture(f'/home/pi/captura_{index}.jpg') # Capturamos!
    sleep(1) # Esperamos 1 segundo para evitar capturas consecutivas
    
    


