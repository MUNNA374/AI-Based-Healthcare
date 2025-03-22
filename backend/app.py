from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
from flask_cors import CORS
from db import save_prediction

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Load AI Model
model = tf.keras.models.load_model("backend/model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    image = request.files['file'].read()
    np_image = np.frombuffer(image, np.uint8)
    img = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224)) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    predicted_class = int(np.argmax(prediction))
    confidence = float(max(prediction[0]))

    # Save to MongoDB
    save_prediction({"prediction": predicted_class, "confidence": confidence})

    return jsonify({"prediction": predicted_class, "confidence": confidence})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
