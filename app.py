import tensorflow as tf
import numpy as np
import cv2
import os

IMG_SIZE = 224

# Load trained model
model = tf.keras.models.load_model("model/bph_model.keras")

def predict_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("❌ Could not read image. Check path.")
        return

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        print(f"\n🟢 BPH Detected! (Confidence: {prediction:.2f})")
    else:
        print(f"\n🔴 Not BPH (Confidence: {1 - prediction:.2f})")


if __name__ == "__main__":
    while True:
        image_path = input("\nEnter image path (or type 'exit' to quit): ")

        if image_path.lower() == "exit":
            print("Exiting...")
            break

        predict_image(image_path)
