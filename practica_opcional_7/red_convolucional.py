from torch import nn

# Creamos la red neuronal convolucional
class ConvolutionalImageClassifier(nn.Module):
    def __init__(self, n_classes=10):
        super(ConvolutionalImageClassifier, self).__init__()
        
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 12 * 12, 10),
            # Con Lazy Linear no hace falta 
            # especificar el tamaño de la entrada
            #nn.LazyLinear(n_classes), 
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x
    
# Creamos la red neuronal convolucional
class ConvolutionalImageClassifierColor(nn.Module):
    def __init__(self):
        super(ConvolutionalImageClassifierColor, self).__init__()
        
        self.conv_layers = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            # nn.Linear(64 * 12 * 12, 10),
            # Con Lazy Linear no hace falta 
            # especificar el tamaño de la entrada
            nn.LazyLinear(10), 
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x