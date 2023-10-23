import requests
import json

def primerObjeto():
    # URL del servicio web
    url = 'http://localhost:5000/directories/'

    # Datos que deseas enviar en formato JSON
    data = {
    "name": "Ejemplo de Objeto",
    "description": "Esto es un objeto de ejemplo"
    }

    # Realizar la solicitud POST
    response = requests.post(url, json=data)

    # Comprobar la respuesta
    if response.status_code == 201:  # 201 significa Created (Creado)
    print("Objeto insertado exitosamente.")
    else:
    print("Error al insertar objeto:", response.status_code)
    print(response.text)  # Imprimir la respuesta en caso de error