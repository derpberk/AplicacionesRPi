from paho.mqtt import client

# Configuración del cliente MQTT
broker_address = "broker.hivemq.com"
port = 1883

# Definimos la función de callback para procesar los mensajes recibidos
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Crear instancia del cliente MQTT
cliente_mqtt = client.Client()
# Conectar al broker
cliente_mqtt.connect(broker_address, port, 60)

# Nos suscribimos al topic
topic = "/etsi/practicas/valor0"
cliente_mqtt.subscribe(topic)
# Iniciamos el loop del cliente MQTT
cliente_mqtt.loop_forever()