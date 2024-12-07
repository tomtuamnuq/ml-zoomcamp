# Use the specified base image
FROM agrigorev/model-2024-hairstyle:v3

# Install required Python libraries
RUN pip install --no-cache-dir \
    https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl \
    pillow
# Copy handler script
COPY handler.py handler.py

# Set environment variable for model path
ENV MODEL_PATH=model_2024_hairstyle_v2.tflite

CMD ["handler.lambda_handler"]
