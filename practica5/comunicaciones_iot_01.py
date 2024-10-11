import time
import paho.mqtt.client as mqtt
import random
import sense_hat

# Configuración del cliente MQTT
broker = "broker.hivemq.com"
port = 1883
topic = "/etsi/practicas/valor0"
client_id = "mqtt_client_sensor"

# Crear instancia del cliente MQTT
client = mqtt.Client(client_id)
# Conectar al broker
client.connect(broker, port, 60)
# Iniciar el loop en segundo plano
client.loop_start()

#Creamos el objeto SenseHat
sense = sense_hat.SenseHat()

try:
    while True:
        # Publicar mensaje al topic
        mensaje = sense.get_temperature()
        client.publish(topic, mensaje)
        print(f"Mensaje enviado: {mensaje}")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Desconectando del broker MQTT...")
    client.loop_stop()
    client.disconnect()

    