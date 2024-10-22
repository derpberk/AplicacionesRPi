import torch
from red_convolucional import ConvolutionalImageClassifier
# Cargar el modelo entrenado

modelo = ConvolutionalImageClassifier(n_classes=10)
modelo.load_state_dict(torch.load('modelo.pt'))
modelo.eval()

# Convertir el modelo a TorchScript usando tracing
example_input = torch.randn(1, 1, 28, 28)  # Ajusta el tamaño del tensor de entrada según tu modelo
traced_script_module = torch.jit.trace(modelo, example_input)

# Guardar el modelo convertido
traced_script_module.save('modelo_jit_arm.pt')