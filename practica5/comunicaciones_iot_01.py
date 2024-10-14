import time
from paho.mqtt import client 
import random
import sense_hat

# Configuración del cliente MQTT
broker = "broker.hivemq.com"
port = 1883
topic = "/etsi/practicas/valor0"
client_id = "mqtt_client_sensor"

# Crear instancia del cliente MQTT
cliente_mqtt = client.Client(client_id)
# Conectar al broker
cliente_mqtt.connect(broker, port, 60)
# Iniciar el loop en segundo plano
cliente_mqtt.loop_start()

#Creamos el objeto SenseHat
sense = sense_hat.SenseHat()

try:
    while True:
        # Publicar mensaje al topic
        mensaje = sense.get_temperature()
        cliente_mqtt.publish(topic, mensaje)
        print(f"Mensaje enviado: {mensaje}")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Desconectando del broker MQTT...")
    cliente_mqtt.loop_stop()
    cliente_mqtt.disconnect()

    