# Use the pre-built base image with the model and DictVectorizer
FROM svizor/zoomcamp-model:3.11.5-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock (if available) from the local directory to the container
COPY Pipfile Pipfile.lock* /app/

# Install dependencies using pipenv in the virtual environment
RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install 

# Copy the Flask app (app.py) into the container
COPY app.py /app/

# Expose port 9696 for the Flask app
EXPOSE 9696

# Run the Flask app with Gunicorn
CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:9696", "app:app"]
