import matplotlib.pyplot as plt
import numpy as np

# Cargar datos desde el archivo CSV
data = np.genfromtxt('datos.csv', delimiter=',')

# Creamos una figura con dos subplots
fig, ax = plt.subplots(2, 1)

# Graficamos la aceleracion en el primer subplot (x, y, z)
ax[0].plot(data[:, 0], data[:, 4:7], label=['x', 'y', 'z'])
ax[0].grid(True)
ax[0].legend()

# Graficamos la aceleracion en el segundo subplot (pitch, roll, yaw)
ax[1].plot(data[:, 0], data[:, 1:4], label=['pitch', 'roll', 'yaw'])
ax[1].grid(True)
ax[1].legend()

plt.show()