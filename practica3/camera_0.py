from picamera2 import Picamera2
from time import sleep

# Instanciamos la clase PiCamera2
camera = Picamera2()
# Configuramos la resolución y rotación de la cámara
camera.resolution = (640,480)
camera.rotation = 180
# Iniciamos la vista previa de la cámara
camera.start_preview(fullscreen=False, window=(30,30,320,240))

for i in range(1,4):
    print(4-i)
    sleep(1)
    
# Capturamos una imagen
camera.capture_file('/home/pi/imagen.jpg')
# Detenemos la vista previa y cerramos la cámara
camera.stop_preview()
# Cerramos la cámara
camera.close()