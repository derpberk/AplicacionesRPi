# -*- coding: utf-8 -*-

import urllib.request, urllib.parse
import random

write_key = "xxxxxxxxxxxxxxx"  # Key para enviar datos

serviceurl = "https://api.thingspeak.com/update?"

def envia_dato(dato):
    params = {"api_key": write_key, "field1": dato}
    req = urllib.parse.urlencode(params)
    url = serviceurl+req
    #print(url) #  descomentar si se quiere ver la url
    try:
        urllib.request.urlopen(url)
        return True
    except:
        print("connection failed")
        return False

temperatura = random.uniform(20, 30) # número aleatorio
res = envia_dato(temperatura)
if res:
    print("Dato enviado correctamente: ", temperatura)
    
    

