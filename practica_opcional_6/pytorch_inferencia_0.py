import time
import torch
import numpy as np
from torchvision import models, transforms
from PIL import Image
# importing the module
import json
import warnings

# Evitamos los warnings innecesarios
warnings.filterwarnings("ignore")

# Habilitamos el cuantificador #
torch.backends.quantized.engine = 'qnnpack'

preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((224,224)),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

net = models.quantization.mobilenet_v2(pretrained=True, quantize=True)
# Just In Case script
net = torch.jit.script(net)

# Cargamos la imagen
image = Image.open('gato.jpg')

# Cargamos los labels de ImageNet
with open('labels.txt') as json_file:
    classes = json.load(json_file)

# Preprocesamos
input_tensor = preprocess(image)

# Creamos un mini-batch (de solo una imagen)
input_batch = input_tensor.unsqueeze(0)

# Ejecutamos el modelo
output = net(input_batch)

# Pintamos los resultados
probs = output[0].softmax(dim=0)
top = torch.argmax(probs)
print(f"Clase: {classes[top]}. Prob: {probs[top] * 100:.2f}")


        
