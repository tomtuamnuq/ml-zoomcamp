# Model Conversion Process

## Question 1: Q1_tf_lite_conversion.py
1. Downloaded the Keras model from the provided URL with `wget`
2. Loaded the model using TensorFlow's Keras model loader
3. Created a TF-Lite converter
4. Converted the model to TF-Lite format
5. Saved the converted model
6. Calculated and compared model sizes

## Question 2: Q2_indices.py
The output of the script will load the tf-lite model and show:

1. Number of inputs
2. Input tensor details
3. Number of outputs
4. Output tensor details

## Question 3 and 4: Q_3_4_example_inference.py
The script showcases how to preprocess the image by using the `interpreter.get_input_details()[0]['shape'][1:3] target size, and how to perform inference with the model.

## Question 5:
This is clear...

## Question 6:

```bash
# Build Docker image
docker build -t hairstyle-inference:v1 .

# Tag image for potential registry push
docker tag hairstyle-inference:v1 username/hairstyle-inference:v1

# Run Docker container locally
docker run -p 8080:8080 \
    hairstyle-inference:v1

# Test container with curl
curl -X POST http://localhost:8080/2015-03-31/functions/function/invocations \
    -H "Content-Type: application/json" \
    -d '{"body": {"image_url":"https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"}}'

```
