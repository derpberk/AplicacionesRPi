from picamera2 import Picamera2, Preview
import gpiozero
from time import sleep
import libcamera

# Creamos un objeto tipo Button 
button = gpiozero.Button("GPIO1", pull_up=False)

# Instanciamos la clase PiCamera2
camera = Picamera2()

# Configuramos la resolución, visualizacion y rotación de la cámara
camera_config = camera.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
camera_config['transform'] = libcamera.Transform(vflip=True) 
camera.configure(camera_config)

for index in range(5):
    
    # Usamos el método wait_for_press() 
    # para esperar a que el botón sea presionado
    button.wait_for_press() 
    # Iniciamos la vista previa de la cámara
    camera.start_preview(Preview.QTGL)
    sleep(5) # Esperamos 5 segundos
    camera.stop_preview() # Detenemos la vista previa
    camera.capture_file(f'/home/pi/captura_{index}.jpg') # Capturamos!
    sleep(1) # Esperamos 1 segundo para evitar capturas consecutivas
    
    
    


