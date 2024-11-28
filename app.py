from flask import Flask, request, jsonify
import pickle
import numpy as np
from flasgger import Swagger
from flask_cors import CORS

with open('model/modelo_tareas.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)
swagger = Swagger(app)
CORS(app)


@app.route('/predecir', methods=['POST'])
def predecir():
    """
    Predicción de tareas.
    ---
    tags:
    - Tareas
    parameters:
      - name: tareas
        in: body
        required: true
        schema:
          type: array
          items:
            type: object
            properties:
              tipo:
                type: number
                example: 1
              tiempo:
                type: number
                example: 16
              peso:
                type: number
                example: 1500
              bugs:
                type: number
                example: 3
    responses:
      200:
        description: Resultados de las predicciones
        schema:
          type: object
          properties:
            resultados:
              type: array
              items:
                type: number
                example: 1.0
    """
    data = request.get_json()

    datos_tareas = np.array([[tarea['tipo'], tarea['tiempo'], tarea['peso'], tarea['bugs']] for tarea in data])

    predicciones = model.predict(datos_tareas)

    return jsonify(predicciones.tolist())

if __name__ == '__main__':
    app.run(debug=True)
