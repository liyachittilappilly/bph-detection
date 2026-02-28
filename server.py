from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)

IMG_SIZE = 224

# Load model once
model = tf.keras.models.load_model("model/bph_model.keras")

def preprocess_image(image):
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    processed = preprocess_image(image)
    prediction = model.predict(processed)[0][0]

    if prediction > 0.5:
        result = "BPH"
        confidence = float(prediction)
    else:
        result = "NOT_BPH"
        confidence = float(1 - prediction)

    return jsonify({
        "prediction": result,
        "confidence": round(confidence, 3)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
