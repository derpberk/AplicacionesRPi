import matplotlib.pyplot as plt
from sense_hat import SenseHat
import time


fig, ax = plt.subplots(2,1) # Creamos una figura con 2 fila y 1 columna

datos_x = []
datos_y = []
datos_y2 = []

sense = SenseHat()
t = 0
while t < 20:
    # Esperamos 1 segundo
    time.sleep(1)
    t += 1
    # Read the temperature
    temp = sense.get_temperature_from_humidity()
    humidity = sense.get_humidity()
    # Añadimos los datos al final de cada lista
    datos_x.append(t)
    datos_y.append(temp)
    datos_y2.append(humidity)
    
# Mostamos los datos
ax[0].plot(datos_x, datos_y, 'b-')
ax[1].plot(datos_x, datos_y2, 'r-')
# Añadimos etiquetas
ax[1].xlabel('Tiempo (s)')
ax[1].ylabel('Humedad (%)')
ax[0].ylabel('Temperatura (C)')
plt.title('Datos vs Tiempo')
# Mostamos la gráfica
plt.show()