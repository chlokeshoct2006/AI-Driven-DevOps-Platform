from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    cpu = data['cpu']
    memory = data['memory']

    prediction = model.predict_proba([[cpu, memory]])[0][1]

    return jsonify({
        "risk": float(prediction)
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)