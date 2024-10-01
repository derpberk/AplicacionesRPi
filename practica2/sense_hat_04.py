import matplotlib.pyplot as plt
from sense_hat import SenseHat
import time

plt.figure() # Creamos una figura
datos_x = []
datos_y = []

sense = SenseHat()
t = 0
while t < 20:
    # Esperamos 1 segundo
    time.sleep(1)
    t += 1
    # Read the temperature
    temp = sense.get_temperature_from_humidity()
    # Añadimos los datos al final de cada lista
    datos_x.append(t)
    datos_y.append(temp)
    
# Mostamos los datos
plt.plot(datos_x, datos_y, 'b-')
# Añadimos etiquetas
plt.xlabel('Tiempo (s)')
plt.ylabel('Temperatura (C)')
plt.title('Temperatura vs Tiempo')
# Mostamos la gráfica
plt.show()