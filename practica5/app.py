from flask import Flask, request, jsonify
from garaje import gar_get_garajes, gar_get_garajes_by_id, gar_get_garajes_parametros, gar_get_garajes_extendido
from vehiculo import veh_add_vehiculo, veh_add_vehiculos

app = Flask(__name__)


@app.route('/garaje', methods=['GET'])
def get_garajes():
    vehiculo_id = request.args.get('vehiculo_id')

    if vehiculo_id:
        return jsonify(gar_get_garajes_parametros(vehiculo_id))
    else:
        return jsonify(gar_get_garajes_extendido())
        #return jsonify(gar_get_garajes())


@app.route('/garaje/<id>', methods=['GET'])
def get_garajes_by_id(id):
    return jsonify(gar_get_garajes_by_id(id))

@app.route('/vehiculo', methods=['POST'])
def add_vehiculo():

    data = request.get_json()
    # propietario_id = data['propietario_id']
    # matricula = data['matricula']
    # tipo_id = data['tipo_id']
    # marca = data['marca']
    # modelo = data['modelo']

    # return jsonify(veh_add_vehiculo(propietario_id, tipo_id, matricula, marca, modelo))
    return jsonify(veh_add_vehiculos(data))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
