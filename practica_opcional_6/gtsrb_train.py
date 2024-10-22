# Importamos los módulos    
import torch
from PIL import Image
from torch import nn,save,load
from torch.optim import Adam
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
from red_convolucional import ConvolutionalImageClassifier
import numpy as np

TRAIN = False

# Seleccionamos el device (GPU, CPU o MPS)
if torch.cuda.is_available():
    device = torch.device('cuda')
elif torch.backends.mps.is_available():
    device = torch.device('mps')
else:
    device = torch.device('cpu')


# Cargamos los datos. En este caso, MNIST.
# Transformamos las imágenes a tensores
transform = transforms.Compose([transforms.ToTensor(), transforms.Resize((32, 32)), transforms.Grayscale(num_output_channels=1)])
# Descargamos el dataset
train_dataset = datasets.GTSRB(root="./data", download=True, split="train", transform=transform)

# Creamos un DataLoader para el dataset de entrenamiento y otro para el de validación
tamaño_dataset = len(train_dataset)
tamaño_train = int(0.8 * tamaño_dataset)
tamaño_val = (tamaño_dataset - tamaño_train)
train_subset, val_subset = torch.utils.data.random_split(train_dataset, [tamaño_train,tamaño_val], generator=torch.Generator().manual_seed(1))
# Creamos los dataloaders
train_loader = DataLoader(train_subset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_subset, batch_size=32, shuffle=True)

# Tomamos 9 imagenes aleatorias del dataset
fig, ax = plt.subplots(3, 3, figsize=(10, 10))
for i in range(3):
    for j in range(3):
        image = train_dataset[i*3 + j][0].moveaxis(0, -1)
        ax[i, j].imshow(image, cmap='gray')
        ax[i, j].set_title(train_dataset[i*3 + j][1])
        ax[i, j].axis('off')
        
plt.show()

# Creamos la red , optimizador y función de pérdida
modelo = ConvolutionalImageClassifier(n_classes=43).to(device)
optimizer = Adam(modelo.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()

def accuracy(predicciones, labels):
    return (torch.argmax(predicciones, dim=1) == labels).float().mean().item()
    

# Entrenamos el modelo
for epoch in range(10):  # Entrenamos durante 10 épocas
    
    loss_train = []
    acc_train = []
    loss_val = []
    acc_val = []
    
    modelo.train()
    for images, labels in train_loader:
        # Pasamos los datos al device
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()  # Reseteamos gradientes
        outputs = modelo(images)  # Hacer predicciones (forward)
        loss = loss_fn(outputs, labels)  # Calcular loss
        loss.backward()  # Calcular gradientes (backward)
        optimizer.step()  # Actualizar parámetros
        # Acumulamos la pérdida
        loss_train.append(loss.item())
        acc_train.append(accuracy(outputs, labels))
        
    # Una vez hemos terminado una época, 
    # evaluamos el modelo en el conjunto de validación
    modelo.eval()
    for images, labels in val_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = modelo(images)
        loss = loss_fn(outputs, labels)
        loss_val.append(loss.item())
        acc_val.append(accuracy(outputs, labels))

    
    print("-"*50)
    print(f"Epoch {epoch + 1}:")
    print(f"Train loss: {np.mean(loss_train):.4f}, Train accuracy: {np.mean(acc_train):.4f}")
    print(f"Val loss: {np.mean(loss_val):.4f}, Val accuracy: {np.mean(acc_val):.4f}")
    
# Guardamos el modelo final
torch.save(modelo.state_dict(), 'modelo_GTSRB.pt')
