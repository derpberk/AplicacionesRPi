# -*- coding: utf-8 -*-

import thingspeak
import time
import random

channel_id = "xxxxx" # identificador del canal
write_key = "xxxxxxxxxxxxxxx" # key para enviar datos

channel = thingspeak.Channel(id=channel_id, api_key=write_key)

for i in range(5):
    dato = random.randint(20, 30) # dato aleatorio
    try:
        response = channel.update({"field1": dato})
        print("Dato enviado: ", dato)
    except:
        print("connection failed")
        break
    time.sleep(15) # tiempo de espera entre envío
    
