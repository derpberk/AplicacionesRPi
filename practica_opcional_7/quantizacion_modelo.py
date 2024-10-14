import torch
import torch.quantization
from red_convolucional import ConvolutionalImageClassifier

# Cargar el modelo
model = ConvolutionalImageClassifier(n_classes=42)  # Modifica según tu modelo
model.load_state_dict(torch.load('modelo_GTSRB.pt', weights_only=True))  # Modifica según tu modelo
model.eval()  # Asegurarse de que el modelo esté en modo evaluación

# Preparar el modelo para cuantización (QAT, Quantization-Aware Training)
model.qconfig = torch.quantization.get_default_qconfig('qnnpack')
torch.backends.quantized.engine = 'qnnpack'

# Fusiones de capas necesarias para una cuantización efectiva
# Fusiones de capas necesarias para una cuantización efectiva



# Preparar el modelo para la cuantización
model = torch.quantization.prepare(model, inplace=False)

print(model)

# Convertir a modelo cuantizado
model = torch.quantization.convert(model, inplace=False)

# Convertir a formato TorchScript
scripted_model = torch.jit.script(model)

# Guardar el modelo cuantizado en TorchScript
scripted_model.save('modelo_cuantizado_jit.pt')

print("Modelo cuantizado y convertido a TorchScript guardado en 'modelo_cuantizado_jit.pt'")
