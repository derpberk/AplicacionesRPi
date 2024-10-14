import requests
import time

# URLs de los servicios web
url_sensor = "http://127.0.0.1:5050/sensor"
url_actuador = "http://127.0.0.1:5050/actuador"

t = 0   
while True:
    time.sleep(1)
    
    # Obtener el valor del sensor
    response = requests.get(url_sensor)
    data = response.json()
    valor_sensor = data['valor_sensor']
    print(f"Valor del sensor: {valor_sensor}")
    valor_actuador = data['valor_actuador']
    print(f"Valor del actuador: {valor_actuador}")
    
    
    if t % 5 == 0:
        # Actualizar el valor del actuador
        nuevo_valor = input("Introduce el nuevo valor del actuador: ")
        response = requests.post(url_actuador, json={'valor_actuador': nuevo_valor})
        print(f"Valor del actuador actualizado a {nuevo_valor}")
        
    t += 1
        
    