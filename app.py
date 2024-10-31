from flask import Flask, request, jsonify
import pickle
import numpy as np

# Cargar el modelo entrenado
with open('model/modelo_tareas.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predecir', methods=['POST'])
def predecir():
    # Obtener los datos de la petición
    data = request.get_json()

    # Convertir los datos en el formato que el modelo espera
    # Ejemplo: {"tipo": 1, "tiempo": 8, "peso": 50, "bugs": 2}
    tipo = data['tipo']
    tiempo = data['tiempo']
    peso = data['peso']
    bugs = data['bugs']

    # Crear un array para hacer la predicción
    datos_prediccion = np.array([[tipo, tiempo, peso, bugs]])

    # Hacer la predicción con el modelo cargado
    prediccion = model.predict(datos_prediccion)

    # Retornar la predicción como respuesta JSON
    return jsonify({'prioridad_predicha': prediccion[0]})

if __name__ == '__main__':
    app.run(debug=True)
