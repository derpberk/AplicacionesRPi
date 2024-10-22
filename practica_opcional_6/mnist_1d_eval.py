# Importamos los módulos    
import torch
from PIL import Image
from torch import nn,save,load
from torch.optim import SGD
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

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
# Descargamos el dataset
test_dataset = datasets.MNIST(root="./data", download=True, train=False, transform=transform)

# Creamos los dataloaders
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)


# Creamos la red neuronal de forma secuencial
modelo = torch.nn.Sequential()
modelo.append(nn.Flatten()) # Aplanamos la imagen (28x28) a un vector (784)
modelo.append(nn.Linear(784, 128)) # Capa lineal con 128 neuronas
modelo.append(nn.ReLU()) # Función de activación ReLU
modelo.append(nn.Linear(128, 10)) # Capa lineal con 10 neuronas (una por cada clase)
modelo = modelo.to(device) # Movemos el modelo a la GPU

modelo.load_state_dict(torch.load("modelo_1D.pt", map_location=device, weights_only=True))

modelo.eval()
predicciones_totales = []
etiquetas_totales = []

for images, labels in test_loader:

	images, labels = images.to(device), labels.to(device)
	print(images.max())
	outputs = modelo(images)

	predicciones_totales.extend(torch.argmax(outputs, dim=1).cpu().detach().numpy().tolist())
	etiquetas_totales.extend(labels.cpu().detach().numpy().tolist())

# Calculamos la matriz de confusión
matrix = confusion_matrix(etiquetas_totales, predicciones_totales)
display = ConfusionMatrixDisplay(matrix)	
display.plot(cmap=plt.cm.Blues)
plt.show()