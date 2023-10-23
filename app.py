from flask import Flask, request, jsonify
from 2 import primerObjeto
app = Flask(__name__)

# Datos de ejemplo para simular una lista de objetos
objects = []

@app.route('/')
def hello():
    return "¡Hola, Mundo!"

# Ruta para responder 'pong'
@app.route('/status/')
def status():
    return "pong"

# Ruta para obtener una lista de objetos
@app.route('/directories/', methods=['GET'])
def get_directories():
    return jsonify(objects)

# Ruta para crear un nuevo objeto
@app.route('/directories/', methods=['POST'])
def create_directory():
    data = request.get_json()
    objects.append(data)
    return jsonify(data), 201

# Ruta para obtener un objeto por su ID
@app.route('/directories/<int:id>', methods=['GET'])
def get_directory(id):
    if 0 <= id < len(objects):
        return jsonify(objects[id])
    else:
        return "Objeto no encontrado", 404

# Ruta para actualizar un objeto por su ID
@app.route('/directories/<int:id>', methods=['PUT'])
def update_directory(id):
    if 0 <= id < len(objects):
        data = request.get_json()
        objects[id] = data
        return jsonify(data)
    else:
        return "Objeto no encontrado", 404

# Ruta para actualizar parcialmente un objeto por su ID
@app.route('/directories/<int:id>', methods=['PATCH'])
def partially_update_directory(id):
    if 0 <= id < len(objects):
        data = request.get_json()
        current_object = objects[id]
        current_object.update(data)
        return jsonify(current_object)
    else:
        return "Objeto no encontrado", 404

# Ruta para eliminar un objeto por su ID
@app.route('/directories/<int:id>', methods=['DELETE'])
def delete_directory(id):
    if 0 <= id < len(objects):
        deleted_object = objects.pop(id)
        return jsonify(deleted_object)
    else:
        return "Objeto no encontrado", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')