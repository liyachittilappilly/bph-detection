import tensorflow as tf
import numpy as np
import cv2
import sys

IMG_SIZE = 224

# Load model
model = tf.keras.models.load_model("model/bph_model.h5")

def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        print(f"BPH detected (confidence: {prediction:.2f})")
    else:
        print(f"Not BPH (confidence: {1 - prediction:.2f})")

if __name__ == "__main__":
    image_path = sys.argv[1]
    predict_image(image_path)
