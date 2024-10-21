# Use official Python 3.11 base image
FROM python:3.11-slim

# Set environment variables to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Install pipenv and system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    wget \
    && pip install --upgrade pip \
    && pip install pipenv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /app

# Download model1.bin and dv.bin files from the provided URLs
RUN PREFIX=https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2024/05-deployment/homework \
    && wget $PREFIX/model1.bin \
    && wget $PREFIX/dv.bin

# Copy the score_subscription.py script from the current working directory on the host
# into the container's /app directory
COPY score_subscription.py /app/

# Ensure the correct Python version is used and install scikit-learn 1.5.2
RUN pipenv --python 3.11 \
    && pipenv install scikit-learn==1.5.2

# Start a bash session as the default command
CMD ["pipenv", "run", "bash"]
