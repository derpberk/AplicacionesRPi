from flask import Flask, jsonify

# Inicializamos la clase Flask
# app representa al servidor.
app = Flask(__name__)

@app.route('/json', methods=['GET'])
def ej_json():
	return jsonify(id=1, nombre="pepe", email="pepe@us.es")

if __name__ == "__main__":
	# Inicializamos el servidor
	app.run(debug=True, port=5002)
