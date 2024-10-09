from sense_hat import SenseHat
import numpy
import time

sense = SenseHat()
datos = []
for t in range(100):
    # Obtener datos del sensor
    ori = sense.get_orientation()
    ace = sense.get_accelerometer_raw()
    
    # Cada fila se compone de:
    # [1 COL (t) +
    #  3 COLS (orientacion) + 
    #  3 COLS (aceleracion)]
    
    datos_fila = [t, ori['pitch'], ori['roll'],  ori['yaw'], 
                  ace['x'],  ace['y'], ace['z']]
    
    # Agregar datos a la lista
    datos.append(datos_fila)
    time.sleep(0.1) # Espera 0.1 segundos
    
# Convertir lista a NumPy array
data = numpy.array(datos)

# Podemos acceder a los datos por fila/columna (como en MatLab)
print(data[:, 1]) # Todas las filas de la columna 1 (pitch)
print(data[0, :]) # La primera fila de todas las columnas

# Guardamos los datos en un archivo CSV con dos decimales
numpy.savetxt('datos.csv', data, delimiter=',', fmt='%.2f')