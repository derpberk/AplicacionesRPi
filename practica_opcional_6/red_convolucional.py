from torch import nn

class DenseImageClassifier(nn.Module):
    def __init__(self, features_entrada = 784, n_classes=10):
        # Inicializamos la clase padre
        super(DenseImageClassifier, self).__init__()
        
        # Definimos las capas
        self.layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, n_classes),
        )

    def forward(self, x):
        x = self.layers(x)
        return x


# Creamos la red neuronal convolucional.
# La clase hereda de nn.Module, que es la clase base 
# para todos los modelos en PyTorch.
class ConvolutionalImageClassifier(nn.Module):
    # El metodo __init__ es el constructor de la clase.
    def __init__(self, n_classes=10): # n_classes es el número de clases
        # Llamamos al constructor de la clase padre
        super(ConvolutionalImageClassifier, self).__init__()
        
        # Definimos las capas convolucionales
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        # Definimos las capas completamente conectadas
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            # Con LazyLinear no hace falta
            # especificar el tamaño de entrada
            # nn.LazyLinear(n_classes),
            nn.Linear(64 * 12 * 12, 128),
            nn.ReLU(),
            nn.Linear(128, n_classes),
        )

    def forward(self, x):
        # El metodo forward define como se calcula la salida
        # a partir de las entradas.
        # out = modelo(in)
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        # Devolvemos la salida
        return x
    