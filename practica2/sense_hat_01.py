from sense_hat import SenseHat

# Instacion de la clase SenseHat
sense = SenseHat()

# Lectura de los sensores
Humedad = sense.get_humidity()
Temp1 = sense.get_temperature_from_humidity()
Temp2 = sense.get_temperature_from_pressure()
Presion = sense.get_pressure()
# Estos sensores devuelven un diccionario con las componentes
Acc = sense.get_accelerometer_raw()
Ori = sense.get_orientation_degrees()
Mag_norte = sense.get_compass()

print(f"Acc: %2.3f %2.3f %2.3f" % (Acc['x'], Acc['y'], Acc['z']))
print(f"Ori: %2.3f %2.3f %2.3f" % (Ori['pitch'], Ori['roll'], Ori['yaw']))
print(f"Mag. Norte: %2.3f" % (Mag_norte))
print(f"Humedad: %2.3f" %Humedad)
print(f"Temperaturas: %2.3f %2.3f" % (Temp1,Temp2))
print(f"Presión: %4.2f" %Presion)

# Mostramos la temperatura en la matriz de leds
TStr = str(round(Temp1,2))
sense.show_message("T : " + TStr)