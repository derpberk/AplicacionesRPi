#Import a JIT model and inference with it

import torch
from PIL import Image

# Load the JIT model
modelo = torch.jit.load('modelo_jit_arm.pt')

# Load the test image and reduce its size to 28x28
img = Image.open('test_5.png').convert('L').resize((28, 28))

# Convert the image to a tensor
img_tensor = torch.tensor([torch.tensor([list(img.getdata())])])

# Process the image with the model
output = modelo(img_tensor)

# Print the output
print(f"Prediction: {torch.argmax(output).item()}")