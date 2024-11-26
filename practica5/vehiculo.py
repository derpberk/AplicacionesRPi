from modelos import Garaje, Vehiculo
import db

def veh_add_vehiculo(propietario_id, tipo_id, matricula, marca, modelo):
    vehiculo = Vehiculo(propietario_id, tipo_id,
                 matricula, marca, modelo)

    data = {    'propietario_id': propietario_id,
            'tipo_id': tipo_id,
            'marca': marca,
            'modelo': modelo,
            'matricula': matricula
    }
    db.session.add(vehiculo)
    db.session.commit()

    return data


def veh_add_vehiculos(datos):

    for d in datos:
        vehiculo = Vehiculo(d.get("propietario_id"), d.get("tipo_id"),
                     d.get("matricula"), d.get("marca"), d.get("modelo"))

        db.session.add(vehiculo)
        db.session.commit()

    return datos