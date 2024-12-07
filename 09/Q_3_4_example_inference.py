import os
import numpy as np
import tensorflow as tf
from io import BytesIO
from urllib import request
from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img 

def load_tflite_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    target_size = tuple(input_details[0]['shape'][1:3])
    
    def predict_image(image_url):
        # Download and preprocess image
        img = download_image(image_url)
        preprocessed_img = prepare_image(img, target_size)

        # Convert to numpy array and normalize
        img_array = np.array(preprocessed_img).astype('float32')
        img_array = img_array / 255.0  # Normalize to [0,1]
        
        # Print first pixel R channel value
        print(f"First pixel R channel value: {img_array[0,0,0]}")

        # Reshape input for model
        input_tensor = np.expand_dims(img_array, axis=0)

        # Run inference
        interpreter.set_tensor(input_details[0]['index'], input_tensor)
        interpreter.invoke()

        # Get output
        output_tensor = interpreter.get_tensor(output_details[0]['index'])
        return output_tensor[0]
    
    return predict_image, target_size

# Load model and create prediction function
MODEL_PATH = 'hairstyle_model.tflite'
predict, input_size = load_tflite_model(MODEL_PATH)

# Example usage
image_url = "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"
probabilities = predict(image_url)

print(f"Input size: {input_size}")
print("\nClass Probabilities:")
for i, prob in enumerate(probabilities):
    print(f"Class {i}: {prob:.4f}")
