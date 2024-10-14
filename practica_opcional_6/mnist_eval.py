from red_convolucional import ConvolutionalImageClassifier
import torch
from PIL import Image
from torch import load
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np

# Seleccionamos el device (GPU, CPU o MPS)
if torch.cuda.is_available():
    device = torch.device('cuda')
elif torch.backends.mps.is_available():
    device = torch.device('mps')
else:
    device = torch.device('cpu')

# Cargamos los datos. En este caso, MNIST.
# Transformamos las imágenes a tensores
transform = transforms.Compose([transforms.ToTensor()])
# Descargamos el dataset de test
test_dataset = datasets.MNIST(root="./data", download=True, train=False, transform=transform)
# Creamos un DataLoader para el dataset de test
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)

# Cargamos el modelo
modelo = ConvolutionalImageClassifier(n_classes=10).to(device)
modelo.load_state_dict(torch.load("modelo.pt", weights_only=True))

# Función de accuracy
def accuracy(predicciones, labels):
    return (torch.argmax(predicciones, dim=1) == labels).float().mean().item()

# Evaluamos el modelo
accuracy_test = []
for images, labels in test_loader:
        # Pasamos los datos al device
        images, labels = images.to(device), labels.to(device)
        outputs = modelo(images)  # Hacer predicciones
        
        # Acumulamos el accuracy
        accuracy_test.append(accuracy(outputs, labels))
        
print(f"Accuracy en test: {np.mean(accuracy_test)}")

# Tomamos 1 imagen aleatoria del dataset
idx = np.random.randint(0, len(test_dataset))
image, label = test_dataset[idx]

# Hacemos la predicción
image = image.unsqueeze(0).to(device)

output = modelo(image)

# Mostramos la imagen y la predicción
plt.imshow(image.squeeze().cpu().numpy(), cmap='gray')
plt.title(f"Predicción: {torch.argmax(output).item()}")
plt.show()
