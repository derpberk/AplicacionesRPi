# -*- coding: utf-8 -*-
import json
import pandas as pd
import thingspeak

channel_id = "xxxxxxx"
read_key = "xxxxxxxxxxx"

channel = thingspeak.Channel(id=channel_id, api_key=read_key)

try:
    response = channel.get()
    print("Datos leídos correctamente")
except:
    print("connection failed")

data=json.loads(response) # leemos el archivo JSON
df = pd.DataFrame(data["feeds"]) # creamos un dataframe
print(df.head())

    
