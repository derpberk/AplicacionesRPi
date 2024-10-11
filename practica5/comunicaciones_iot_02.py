import paho.mqtt.client as mqtt

# Definimos la función de callback para procesar los mensajes recibidos
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Creamos el cliente MQTT
client = mqtt.Client()

# Asignamos la función de callback al cliente
client.on_message = on_message

# Nos conectamos al broker MQTT
broker_address = "broker.hivemq.com"
port = 1883
client.connect(broker_address, port)

# Nos suscribimos al topic
topic = "/etsi/practicas/valor0"
client.subscribe(topic)

# Iniciamos el loop del cliente MQTT
client.loop_forever()