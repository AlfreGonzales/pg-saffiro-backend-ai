from flask import Flask, request, jsonify
import pickle
import numpy as np

# Cargar el modelo entrenado
with open('model/modelo_tareas.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predecir', methods=['POST'])
def predecir():
    # Obtener los datos de la petición, que ahora se espera que sea una lista de objetos
    data = request.get_json()

    # Convertir los datos en un array de predicción adecuado para el modelo
    datos_tareas = np.array([[tarea['tipo'], tarea['tiempo'], tarea['peso'], tarea['bugs']] for tarea in data])

    # Hacer las predicciones con el modelo cargado
    predicciones = model.predict(datos_tareas)

    # Retornar las predicciones como respuesta JSON
    return jsonify({'resultados': predicciones.tolist()})

if __name__ == '__main__':
    app.run(debug=True)

