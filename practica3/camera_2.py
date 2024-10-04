import time

from picamera2 import Picamera2
from picamera2.encoders import Encoder, H264Encoder, Quality
import gpiozero

# Instanciamos la clase PiCamera2
picam2 = Picamera2()
# Creamos el botón conectado al GPIO1 con pull-up
button = gpiozero.Button("GPIO1", pull_up=True)

# Creamos una configuración de video
video_config = picam2.create_video_configuration()
video_config.resolution = (640, 480)
video_config.framerate = 24
video_config.rotation = 180
# Ajustamos la resolución y el framerate
picam2.configure(video_config)

# Si queremos grabar en formato RAW
# encoder = Encoder()
# Creamos un objeto tipo H264Encoder (compresor de video)
encoder = H264Encoder(10000000)

# Iniciamos la grabación de video
button.wait_for_press() # Esperamos a que el botón sea presionado
print("Grabando video")
picam2.start_recording(encoder, '/home/pi/video.h264', quality=Quality.HIGH)
button.wait_for_press() # Esperamos a que el botón sea presionado
print("Deteniendo grabación")
picam2.stop_recording()