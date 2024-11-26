from flask import Flask, jsonify

# Inicializamos la clase Flask
# app representa al servidor.
app = Flask(__name__)

@app.route('/parametros/<param>', methods=['GET'])
def ej_parametros(param):
	return jsonify(id=1, parametro=param)

if __name__ == "__main__":
	# Inicializamos el servidor
	app.run(debug=True, port=5002)
