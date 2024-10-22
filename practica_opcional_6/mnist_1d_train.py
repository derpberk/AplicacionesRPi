# Importamos los módulos    
import torch
from torch import nn, save
from torch.optim import SGD
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score

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
train_dataset = datasets.MNIST(root="./data", download=True, train=True, transform=transform)

# Tomamos 9 imagenes aleatorias del dataset
fig, ax = plt.subplots(3, 3, figsize=(10, 10))
for i in range(3):
    for j in range(3):
        ax[i, j].imshow(train_dataset[i*3 + j][0].squeeze(), cmap='gray')
        ax[i, j].set_title(train_dataset[i*3 + j][1])
        ax[i, j].axis('off')
        
plt.show()

# Creamos un DataLoader para el dataset de entrenamiento y otro para el de validación
tamaño_dataset = len(train_dataset)
tamaño_train = int(0.8 * tamaño_dataset)
tamaño_val = (tamaño_dataset - tamaño_train)
train_subset, val_subset = random_split(train_dataset, [tamaño_train, tamaño_val], generator=torch.Generator().manual_seed(1))

# Creamos los dataloaders
train_loader = DataLoader(train_subset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_subset, batch_size=32, shuffle=True)

# Creamos la red neuronal de forma secuencial
modelo = torch.nn.Sequential()
modelo.append(nn.Flatten()) # Aplanamos la imagen (28x28) a un vector (784)
modelo.append(nn.Linear(784, 128)) # Capa lineal con 128 neuronas
modelo.append(nn.ReLU()) # Función de activación ReLU
modelo.append(nn.Linear(128, 10)) # Capa lineal con 10 neuronas (una por cada clase)
modelo = modelo.to(device) # Movemos el modelo a la GPU

# Creamos el optimizador (SGD) y la función de pérdida
optimizer = SGD(modelo.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()

# Inicializamos las listas de loss y accuracy
epoch_loss_train = []
epoch_loss_val = []
epoch_acc_train = []
epoch_acc_val = []

# Entrenamos el modelo
for epoch in range(10):  # Entrenamos durante 10 épocas
	
	# Inicializamos las listas de loss y accuracy
	loss_train = []
	acc_train = []
	loss_val = []
	acc_val = []
	
	modelo.train() # Ponemos el modelo en modo entrenamiento
	for images, labels in train_loader:
		# Pasamos los datos al device
		images, labels = images.to(device), labels.to(device)
		outputs = modelo(images)  # Hacer predicciones (forward)
		optimizer.zero_grad()  # Reseteamos gradientes
		loss = loss_fn(outputs, labels)  # Calcular loss
		loss.backward()  # Calcular gradientes (backward)
		optimizer.step()  # Actualizar parámetros
		# Acumulamos la pérdida
		loss_train.append(loss.item())
		# Predecimos las etiquetas
		predictions = torch.argmax(outputs, dim=1).cpu().detach().numpy()
		# Calculamos la precisión
		acc_train.append(accuracy_score(predictions, labels.cpu()))
		
	# Una vez hemos terminado una época, 
	# evaluamos el modelo en el conjunto de validación
	modelo.eval()
	for images, labels in val_loader:
		images, labels = images.to(device), labels.to(device)
		outputs = modelo(images)
		loss = loss_fn(outputs, labels)
		loss_val.append(loss.item())
		# Predecimos las etiquetas - Tomamos la clase con mayor probabilidad
		predictions = torch.argmax(outputs, dim=1).cpu().detach().numpy()
		acc_val.append(accuracy_score(predictions, labels.cpu()))

	print("-"*50)
	print(f"Epoch {epoch + 1}:")
	print(f"Train loss: {np.mean(loss_train):.4f}, Train accuracy: {np.mean(acc_train):.4f}")
	print(f"Val loss: {np.mean(loss_val):.4f}, Val accuracy: {np.mean(acc_val):.4f}")

	# Guardamos los valores de loss y accuracy
	epoch_loss_train.append(np.mean(loss_train))
	epoch_loss_val.append(np.mean(loss_val))
	epoch_acc_train.append(np.mean(acc_train))
	epoch_acc_val.append(np.mean(acc_val))
	
# Guardamos el modelo final
torch.save(modelo.state_dict(), 'modelo_1D.pt')

# Representamos el loss:
with plt.style.context('bmh'):
	plt.figure(figsize=(5, 4))
	plt.plot(epoch_loss_train, label="Train loss")
	plt.plot(epoch_loss_val, label="Val. loss")
	plt.xlabel("Epoch")
	plt.ylabel("Loss")
	plt.legend()
	plt.savefig("loss_1D.png")
	plt.show()

# Representamos el accuracy:
with plt.style.context('bmh'):
	plt.figure(figsize=(5, 4))
	plt.plot(epoch_acc_train, label="Train Accuracy")
	plt.plot(epoch_acc_val, label="Val. Accuracy")
	plt.xlabel("Epoch")
	plt.ylabel("Accuracy")
	plt.legend()
	plt.savefig("accuracy_1D.png")
	plt.show()

# Matri
