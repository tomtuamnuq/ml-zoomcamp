import tensorflow as tf

# Load the TF-Lite model
interpreter = tf.lite.Interpreter(model_path='hairstyle_model.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Print input and output details
print("Input Details:")
for i, input_detail in enumerate(input_details):
    print(f"Input {i}: {input_detail}")

print("\nOutput Details:")
for i, output_detail in enumerate(output_details):
    print(f"Output {i}: {output_detail}")
