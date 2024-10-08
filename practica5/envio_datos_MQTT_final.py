# -*- coding: utf-8 -*-
import paho.mqtt.publish as publish
import random

channelID = "xxxxxx" # canal

useUnsecuredTCP = True # comunicación por TCP
useUnsecuredWebsockets = False # comunicación por socket web
mqtthost = "mqtt3.thingspeak.com"

mqtt_client_ID = "xxxxxxxxxxxxxxxx" # copiar y pegar de thingspeak
mqtt_username  = "xxxxxxxxxxxxxxxx"
mqtt_password  = "xxxxxxxxxxxxxxxx"

if useUnsecuredTCP:
    tTransport = "tcp"
    tPort = 1883
    tTLS = None

if useUnsecuredWebsockets:
    tTransport = "websockets"
    tPort = 80
    tTLS = None

dato = random.randint(20, 30)        
topic = "channels/" + channelID + "/publish"
tPayload = "field1=" + str(dato)

try:
    publish.single(topic, payload=tPayload, hostname=mqtthost, port=tPort, 
                   tls=tTLS, transport=tTransport, client_id=mqtt_client_ID,
                   auth={'username':mqtt_username,'password':mqtt_password})
    print("Dato publicado: ", dato)
    
except:
    print ("Fallo al publicar los datos")
