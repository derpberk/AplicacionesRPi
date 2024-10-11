from flask import Flask, jsonify, request
import random

app = Flask(__name__)

valor_actuador = 0

@app.route('/sensor', methods=['GET'])
def get_random_value():
    # Obtener el valor del sensor (aleatorio)
    random_value = random.randint(1, 100)
    # Devolver el valor del sensor y el valor del actuador
    return jsonify({'valor_sensor': random_value, 
                    'valor_actuador': valor_actuador})

@app.route('/actuador', methods=['POST', 'GET'])
def update_random_value():
    global valor_actuador
    # Actualizar el valor del actuador
    valor_actuador = request.json['valor_actuador']
    print(f"Nuevo valor recibido: {valor_actuador}")
    
    return jsonify({'valor_actuador': valor_actuador})

if __name__ == '__main__':
    app.run(debug=True, port=5050)