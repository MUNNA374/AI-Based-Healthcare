from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
from config import patients_collection  # Import MongoDB

app = Flask(__name__)

# Load AI Model
model = tf.keras.models.load_model("model.h5")

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
    
    # Save result in MongoDB
    record = {
        "prediction": prediction.tolist(),
        "patient_id": "12345",
        "image_name": request.files['file'].filename
    }
    patients_collection.insert_one(record)

    return jsonify({"prediction": prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
