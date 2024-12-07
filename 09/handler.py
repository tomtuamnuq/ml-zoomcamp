import json
import os
import numpy as np
from tflite_runtime.interpreter import Interpreter
import urllib.request
from PIL import Image
from io import BytesIO

# Global model resources
INTERPRETER = None
INPUT_DETAILS = None
OUTPUT_DETAILS = None
TARGET_SIZE = None

def validate_image_url(url):
    try:
        # Head request to validate URL and check image type
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req) as response:
            content_type = response.headers.get('Content-Type', '')
            
        # Validate image mime types
        valid_image_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
        return content_type in valid_image_types

    except Exception:
        return False

def download_image(url):
    if not validate_image_url(url):
        raise ValueError("Invalid image URL")
    
    with urllib.request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def load_model():
    global INTERPRETER, INPUT_DETAILS, OUTPUT_DETAILS, TARGET_SIZE
    
    if INTERPRETER is None:
        model_path = os.getenv('MODEL_PATH', 'hairstyle_model.tflite')
        INTERPRETER = Interpreter(model_path=model_path)
        INTERPRETER.allocate_tensors()
        
        INPUT_DETAILS = INTERPRETER.get_input_details()
        OUTPUT_DETAILS = INTERPRETER.get_output_details()
        TARGET_SIZE = tuple(INPUT_DETAILS[0]['shape'][1:3])
    
    return INTERPRETER, INPUT_DETAILS, OUTPUT_DETAILS, TARGET_SIZE

def lambda_handler(event, context):
    # Extract image URL from event
    body = event.get('body', '{}')
    if isinstance(body, str):
        body = json.loads(body)

    image_url = body.get('image_url')
    
    if not image_url:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No image URL provided'})
        }
    
    # Load model (cached)
    interpreter, input_details, output_details, target_size = load_model()
    
    try:
        # Download and preprocess image
        img = download_image(image_url)
        preprocessed_img = prepare_image(img, target_size)
        
        # Convert to numpy array and normalize
        img_array = np.array(preprocessed_img).astype('float32')
        img_array = img_array / 255.0
        
        # Reshape input for model
        input_tensor = np.expand_dims(img_array, axis=0)
        
        # Run inference
        interpreter.set_tensor(input_details[0]['index'], input_tensor)
        interpreter.invoke()
        
        # Get output probabilities
        output_tensor = interpreter.get_tensor(output_details[0]['index'])
        probability = output_tensor[0][0]
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'probability': str(probability),
            })
        }
    
    except ValueError as ve:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(ve)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
