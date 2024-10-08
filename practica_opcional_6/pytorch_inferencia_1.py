import time
import torch
import numpy as np
from torchvision import models, transforms
import libcamera
from picamera2 import Picamera2
import json

# Opening JSON file
with open('labels.txt') as json_file:
    classes = json.load(json_file)
    

picam2 = Picamera2()
# Configuramos la resolución y formato de la cámara
config = {"format": 'RGB888', "size": (224, 224)}
picam2.configure(picam2.create_preview_configuration(main=config)) #, transform=libcamera.Transform(vflip=True)))
# Iniciamos la vista previa de la cámara
picam2.start()

torch.backends.quantized.engine = 'qnnpack'

preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

net = models.quantization.mobilenet_v2(pretrained=True, quantize=True)
# jit model to take it from ~20fps to ~30fps
net = torch.jit.script(net)

started = time.time()
last_logged = time.time()
frame_count = 0

with torch.no_grad():
    while True:
        # read frame
        image = picam2.capture_array()

        # preprocess
        input_tensor = preprocess(image)

        # create a mini-batch as expected by the model
        input_batch = input_tensor.unsqueeze(0)

        # run model
        output = net(input_batch)
        
        probs = output[0].softmax(dim=0)
        top = torch.argmax(probs)
        print(f"Clase: {classes[top]}. Prob: {probs[top] * 100:.2f}")

        # log model performance
        frame_count += 1
        now = time.time()
        if now - last_logged > 1:
            print(f"{frame_count / (now-last_logged)} fps")
            last_logged = now
            frame_count = 0
        
