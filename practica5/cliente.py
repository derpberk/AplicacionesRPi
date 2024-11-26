

import requests

# Creamos la petición HTTP con GET:

# Función encargada de realizar una petición a un
# determinado endpoint --> url
def cliente_get(url):
    peticion = requests.get(url)

    # datos --> lista de diccionarios --> Fue creado en gar_get_garajes_extendido
    # o gar_get_garajes
    datos = peticion.json()

    # Para recorrer esa lista, diccionario a diccionario
    for d in datos:
        # d representa a cada diccionario
        print(d)

# Llamada a la función
# cliente_get("http://127.0.0.1:5002/garaje")


# Función encargada de realizar una petición a un
# determinado endpoint --> url, aplicando un filtro
def cliente_get_filtros(url, parametros):
    peticion = requests.get(url, params=parametros)

    # datos --> lista de diccionarios --> Fue creado en gar_get_garajes_extendido
    # o gar_get_garajes
    datos = peticion.json()

    # Para recorrer esa lista, diccionario a diccionario
    for d in datos:
        # d representa a cada diccionario
        print(d)

# Llamada a la función
# Objetivo: http://127.0.0.1:5002/garaje?vehiculo_id=2
parametros = {"vehiculo_id": 2}
# cliente_get_filtros("http://127.0.0.1:5002/garaje", parametros)


# Función encargada de realizar una insercion de datos,
# a través de un POST
def cliente_insertar(url, datos):
# Creamos la peticion HTTP con POST:
    resp = requests.post(url, json=datos)
    print(resp)

datos = {
        "propietario_id": 3,
        "tipo_id": 1,
        "matricula": "1",
        "marca": "Audi",
        "modelo": "A3"
    }
#cliente_insertar("http://127.0.0.1:5002/vehiculo", datos)

# Función encargada de realizar una insercion de varios
# vehiculos a la vez, a través de un POST
def cliente_insertar_varios(url, datos):
# Creamos la peticion HTTP con POST:
    resp = requests.post(url, json=datos)
    print(resp)

# lista de diccionarios
datos = [{
        "propietario_id": 3,
        "tipo_id": 1,
        "matricula": "1",
        "marca": "Audi",
        "modelo": "A3"
    },
{
        "propietario_id": 1,
        "tipo_id": 1,
        "matricula": "2",
        "marca": "Skoda",
        "modelo": "Rapid"
    }
]
cliente_insertar_varios("http://127.0.0.1:5002/vehiculo", datos)
