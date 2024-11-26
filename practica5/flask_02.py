from flask import Flask

# Inicializamos la clase Flask
# app representa al servidor.
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hola_mundo():
	return "Hola Mundo"

if __name__ == "__main__":
	# Inicializamos el servidor
	app.run(debug=True, port=5002)
