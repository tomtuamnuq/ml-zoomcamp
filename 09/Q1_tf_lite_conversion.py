import tensorflow as tf
import os

model_path = "model_2024_hairstyle.keras"

# Load the Keras model
model = tf.keras.models.load_model(model_path)

# Convert to TF-Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TF-Lite model
with open('hairstyle_model.tflite', 'wb') as f:
    f.write(tflite_model)

# Get model sizes
keras_model_size = os.path.getsize(model_path) / (1024 * 1024)  # MB
tflite_model_size = os.path.getsize('hairstyle_model.tflite') / (1024 * 1024)  # MB

print(f"Original Keras Model Size: {keras_model_size:.2f} MB")
print(f"Converted TF-Lite Model Size: {tflite_model_size:.2f} MB")
