from modelos import Garaje, Vehiculo
import db


def gar_get_garajes():
    # Ejecuta una consulta para recuperar todos los registros de la tabla garaje
    # garajes es una lista de objetos Garaje, con tantos elementos como registros
    # tenga la tabla
    garajes = db.session.query(Garaje).all()

    data = []

    # Se va a construir una lista de diccionarios
    # Cada diccionario representa un registro de la tabla
    for garaje in garajes:
        data.append({'id': garaje.id,
                   'vehiculo_id': garaje.vehiculo_id,
                   'n_plaza': garaje.n_plaza
                   })

    return (data)

# Será usado cuando se filtre por el vehiculo_id
def gar_get_garajes_parametros(vehiculo_id):
    garajes = db.session.query(Garaje).filter(Garaje.vehiculo_id == vehiculo_id).all()

    data = []

    for garaje in garajes:
        data.append({'id': garaje.id,
                     'vehiculo_id': garaje.vehiculo_id,
                     'n_plaza': garaje.n_plaza
                     })
    return data

def gar_get_garajes_by_id(id_buscado):
    # Garajes es una lista de objetos del tipo Garaje,
    # cuyo registro id coincide con id_buscado
    garajes = db.session.query(Garaje).filter(Garaje.id == id_buscado).all()

    data = []

    # Se va a construir una lista de diccionarios
    # Cada diccionario representa un registro de la tabla
    for garaje in garajes:
        data.append({'id': garaje.id,
                     'vehiculo_id': garaje.vehiculo_id,
                     'n_plaza': garaje.n_plaza
                     })
    return data

def gar_get_garajes_extendido():
    # Se hace un join de ambas tablas, a través de las clases Garaje y Vehiculo
    garajes = db.session.query(Garaje, Vehiculo).join(Garaje, Garaje.vehiculo_id
                                                      == Vehiculo.id).all()

    data = []
    # Se va a construir una lista de diccionarios
    # Cada diccionario representa un registro de la tabla (garaje-vehiculo)
    for garaje in garajes:
        data.append({'id': garaje.Garaje.id,
                     'vehiculo_id': garaje.Garaje.vehiculo_id,
                     'n_plaza': garaje.Garaje.n_plaza,
                     'propietario_id': garaje.Vehiculo.propietario_id,
                     'marca': garaje.Vehiculo.marca,
                     'modelo': garaje.Vehiculo.modelo,
                     'matricula': garaje.Vehiculo.matricula
                     })

    return (data)