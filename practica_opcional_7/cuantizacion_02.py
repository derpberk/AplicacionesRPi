import torch
import torch.nn as nn
from torchvision import models, transforms
from red_convolucional import ConvolutionalImageClassifier
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from picamera2 import Picamera2
import libcamera

# Creamos el thread the la ventana de OpenCV
cv2.startWindowThread()
# Creamos el objeto de la RaspiCam
picam2 = Picamera2()
# Modificamos el framrate (fps)
picam2.video_configuration.controls.FrameRate = 25.0
# Configuramos la resolución y formato de la cámara
config = {"format": 'RGB888', "size": (640, 480),}
picam2.configure(
	picam2.create_preview_configuration(
		main=config,
		transform=libcamera.Transform(vflip=True)))
# Iniciamos la vista previa de la cámara
picam2.start()

device = torch.device('cpu')

tipo_modelo = 'torch'

if tipo_modelo == 'torch':
    # Cargar modelo preentrenado modelo_conv.pt
    model = ConvolutionalImageClassifier(n_classes=10).to(device)
    model.load_state_dict(torch.load('modelo_conv.pt', weights_only=True, map_location=device))
    model.eval()
elif tipo_modelo == 'torchscript':
    # Cargar modelo TorchScript
    model = torch.jit.load('modelo_torchscript.pt', map_location=device)

print("Presiona 'q' para salir.")

while True:
    # Leer la imagen de la webcam
    frame = picam2.capture_array()

    if not ret:
        break

    # Cambiar a blanco y negro
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    # Tomamos el centro de la pantalla
    frame_gray = frame_gray[int(640*0.33):int(640*0.66), int(480*0.33):int(480*0.66)]
    # Pasamos a una imagen de 28x28
    frame_gray = cv2.resize(frame_gray, (28, 28)).astype(np.float32)
    # Minmax-normalización
    frame_gray = (frame_gray - frame_gray.min()) / (frame_gray.max() - frame_gray.min() + 1)
    # Invertimos la imagen
    frame_gray = 1 - frame_gray
    # Ponemos a 0 (negro) el fondo
    frame_gray[frame_gray < 0.33] = 0.0
    # Pasamos a tensor
    frame_gray = torch.Tensor(frame_gray)
    # Añadimos una dimensión en la posición 1: (28,28) -> (1,1,28,28)
    frame_gray = frame_gray.reshape(1, 1, 28, 28)


    # Hacer predicción
    outputs = model(frame_gray)
    # Obtenemos la probabilidad con un softmax
    probs = torch.nn.functional.softmax(outputs, dim=1).squeeze(0)
    # Obtener la predicción más probable
    max_prob, class_predicted = torch.max(outputs, 1)
    
    if max_prob > 0.5:
    
        prediccion = str(class_predicted.item())
        print(prediccion)
        # Mostrar la predicción en la imagen de la webcam
        cv2.putText(frame, prediccion, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
        1, (0, 255, 0), 2, cv2.LINE_AA)

    # Mostrar el video de la webcam
    cv2.imshow('Webcam', frame)
    # Convertimos de numpy a cv2
    image_cv2 = frame_gray.squeeze().numpy()
    image_cv2 = (image_cv2 * 255).astype(np.uint8)
    # Resize
    image_cv2 = cv2.resize(image_cv2, (512, 512), 0, 0, interpolation = cv2.INTER_NEAREST)
    cv2.imshow('Input', image_cv2)
    

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
