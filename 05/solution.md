# Machine Learning Zoomcamp Homework - Module 5: Deployment

## Introduction

For this homework, I created a custom Dockerfile to perform the tasks for Questions 1 to 4 without needing to install Python 3.11 and Pipenv directly on the host system. I used Docker to encapsulate the environment, ensuring consistent results and easy reproducibility.

---

## Installation of Docker on Arch Linux

If you're using Arch Linux, you can install Docker with the following commands:

```bash
yay -S docker
sudo usermod -a -G docker mot
sudo systemctl start docker.service
```

---

## Question 1: Install Pipenv

- **Task**: Install Pipenv and find out the version.
- **Solution**: Instead of installing Pipenv on the host machine, I built and ran a Docker container for the task.

**Steps:**
```bash
docker build -t python-pipenv-ml-05 .
docker run -it python-pipenv-ml-05:latest
```

**Inside the container**:
```bash
pipenv --version
```

**Answer**:
```
pipenv, version 2024.1.0
```

---

## Question 2: Install Scikit-Learn

- **Task**: Use Pipenv to install Scikit-Learn version 1.5.2 and find the first hash for `scikit-learn` in `Pipfile.lock`.

**Inside the container**:
```bash
cat Pipfile.lock
```

**Answer**:
```
"sha256:03b6158efa3faaf1feea3faa884c840ebd61b6484167c711548fce208ea09445"
```

---

## Question 3: Load the Model and Score a Client

- **Task**: Write a script to load the model using `pickle` and predict the subscription probability for a client with the following details:

```json
{
  "job": "management",
  "duration": 400,
  "poutcome": "success"
}
```

**Still inside the container**:
```bash
python score_subscription.py '{"job": "management", "duration": 400, "poutcome": "success"}'
```

**Answer**:
```
Predicted probability of subscription: 0.759
```

---

## Question 4: Skipped

I skipped this question and proceeded directly to serving the model in Docker (Question 6).

---

## Question 5: Base Image Size

- **Task**: Pull the `svizor/zoomcamp-model:3.11.5-slim` Docker image and find its size.

**Steps**:
```bash
docker pull svizor/zoomcamp-model:3.11.5-slim
docker images
```

**Answer**:
```
svizor/zoomcamp-model   3.11.5-slim   975e7bdca086   2 days ago   130MB
```

---

## Question 6: Serve the Model as a Web Service

- **Task**: Serve the model as a web service using Flask and Gunicorn, then score the client again via a POST request.

**Steps**:
```bash
cd flask
docker build -t flask-gunicorn-app .
docker run -it -p 9696:9696 flask-gunicorn-app:latest
```

**POST Request from the host machine**:
```bash
curl -X POST http://localhost:9696/predict \
    -H "Content-Type: application/json" \
    -d '{"job": "management", "duration": 400, "poutcome": "success"}'
```

**Response**:
```json
{"subscription_probability": 0.756743795240796}
```

---

## Conclusion

Through the use of Docker, I managed to package and deploy the model in a controlled environment. This approach ensures consistency, regardless of the host system setup, and makes it easy to reproduce the results by anyone following these steps.
