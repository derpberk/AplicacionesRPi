from flask import Flask, request, render_template_string, jsonify
import random

app = Flask(__name__)

# HTML template
html_template = """
<!doctype html>
<meta http-equiv="refresh" content="3" />  
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Actuador</title>
    </head>
    <body>
        <div class="container">
            <h1>Valor del Actuador</h1>
            <p>      {{ value }}      </p>
        </div>
    </body>
</html>
"""

# Variable global
valor_actuador = 0

@app.route('/actuador', methods=['POST', 'GET'])
def actuador():
    global valor_actuador
    value = request.json['valor_actuador']
    valor_actuador = value
    return jsonify({'valor_sensor': value})
    
@app.route('/sensor', methods=['GET'])
def sensor():
    global valor_actuador
    # Obtener el valor del sensor (aleatorio)
    random_value = random.randint(1, 100)
    # Devolver el valor del sensor y el valor del actuador
    return jsonify({'valor_sensor': random_value, 
                    'valor_actuador': valor_actuador})
    
@app.route('/')
def home():
    global valor_actuador
    return render_template_string(html_template, value=valor_actuador)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5050)