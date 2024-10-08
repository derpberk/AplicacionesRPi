# -*- coding: utf-8 -*-
import urllib.request, urllib.parse
import json
import pandas as pd

read_key = "xxxxxxxxxxxxx"

serviceurl = "https://api.thingspeak.com/channels/1444384/feeds.json?"

def lee_datos():
    params = {"api_key": read_key, "results": 100} 
    req = urllib.parse.urlencode(params)
    url = serviceurl+req
    print(url)
    try:
        respuesta = urllib.request.urlopen(url)
        return respuesta # devolvemos los datos
    except:
        print("connection failed")
        return -1

respuesta = lee_datos()
if (respuesta!=-1):
    data=json.loads(respuesta.read()) # convertimos a diccionario
    print(data.keys()) # tenemos dos claves: channel y feeds
    print(data["feeds"]) # muestra los datos 
    df = pd.DataFrame(data["feeds"]) # creamos un dataframe
    print(df.head())
    
