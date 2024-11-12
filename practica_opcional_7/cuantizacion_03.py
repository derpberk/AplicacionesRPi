import torch
from torch.ao.quantization import (
  get_default_qconfig_mapping,
  QConfigMapping,
)
import torch.ao.quantization.quantize_fx as quantize_fx
import copy
import torchvision
import os

cuantizacion_estatica = True

# Cargamos un modelo cualquiera, ya preentrenado
modelo_sin_cuantizar = torchvision.models.mobilenet_v2(pretrained=True)

# Lo copiamos para cuantizarlo y comparar el tamaño #
modelo_a_cuantizar = copy.deepcopy(modelo_sin_cuantizar)
modelo_a_cuantizar.eval()

# Para cuantización dinámica (Se cuantizan pesos pero no activaciones):
if not cuantizacion_estatica:
	qconfig_mapping = QConfigMapping().set_global(torch.ao.quantization.default_dynamic_qconfig)
else:
	# Para cuantización estática (Se cuantiza todo) con QNNPACK (arm64)
	torch.backends.quantized.engine = 'qnnpack'
	qconfig_mapping = get_default_qconfig_mapping("qnnpack")


# Preparamos el modelo para cuantizarlo
example_inputs = torch.randn(16, 3, 224, 224)
modelo_preparado = quantize_fx.prepare_fx(modelo_a_cuantizar, qconfig_mapping, example_inputs)
# Lo cuantizamos
modelo_cuantizado = quantize_fx.convert_fx(modelo_preparado)

if cuantizacion_estatica:
	# Le pasamos un ejemplo para que sepa las dimensiones de las entradas y calibre los rangos
	for _ in range(10):
		example_inputs = torch.randn(16, 3, 224, 224)
		output = modelo_cuantizado(example_inputs)

def print_model_size(mdl):
	torch.save(mdl.state_dict(), "tmp.pt")
	print("Tamño en MB: %.2f MB" %(os.path.getsize("tmp.pt")/1e6))
	os.remove('tmp.pt')


print("Tamaños de los modelos:")
print_model_size(modelo_sin_cuantizar)
print_model_size(modelo_cuantizado)

# Pasamos el modelo a jit
modelo_cuantizado = torch.jit.script(modelo_cuantizado)

# Guardamos el modelo cuantizado
torch.jit.save(modelo_cuantizado, 'modelo_cuantizado_mobilenet.pth')
