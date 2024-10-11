from flask import Flask, request, render_template_string, jsonify
import random
import sense_hat


app = Flask(__name__)

# HTML template
html_template = """
<!doctype html>
<meta http-equiv="refresh" content="3" />  
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" 
        content="width=device-width, 
        initial-scale=1, 
        shrink-to-fit=no">
        <title>Actuador</title>
    </head>
    <body>
        <div class="container">
            <h1>Valor del Sensor</h1>
            <p>      {{ sensor }}      </p>
            <h1>Valor en pantalla</h1>
            <p>      {{ caracter }}      </p>
        </div>
    </body>
</html>
"""

# Variable global
valor_actuador = 'X'
valor_sensor = 0
sense = sense_hat.SenseHat()

@app.route('/actuador', methods=['POST'])
def actuador():
    global valor_actuador, valor_sensor
    valor_actuador = request.json['valor_actuador']
    # Actualizar el valor de la pantalla
    sense.show_letter(valor_actuador)
    return jsonify({'valor_actuador': valor_actuador})

    
@app.route('/sensor', methods=['GET'])
def sensor():
    global valor_actuador, valor_sensor
    # Obtener el valor del sensor
    valor_sensor = sense.get_temperature()
    # Devolver el valor del sensor y el valor del actuador
    return jsonify({'valor_sensor': valor_sensor, 
                    'valor_actuador': valor_actuador})
    
@app.route('/')
def home():
    global valor_actuador, valor_sensor
    valor_sensor = sense.get_temperature()
    return render_template_string(html_template, 
                                    sensor=valor_sensor, 
                                    caracter = valor_actuador)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)