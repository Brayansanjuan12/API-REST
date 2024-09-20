from flask import Flask, request, jsonify

# Inicializa la aplicación Flask
app = Flask(__name__)

# Ruta para el método GET
@app.route('/saludo', methods=['GET'])
def saludo():
    # Devuelve un saludo como respuesta
    return jsonify({"mensaje": "¡Hola, bienvenido a la API!"})

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)


