#### Step 1: Install Kind

First, I installed Kind (Kubernetes IN Docker) using the following command:

```sh
go install sigs.k8s.io/kind@v0.25.0
```

After installation, I verified the version to ensure it was installed correctly:

```sh
kind --version
```

#### Step 2: Navigate to the Project Directory

I navigated to the directory containing the assignment files:

```sh
cd cohorts/2024/05-deployment/homework
```

#### Step 3: Build the Docker Image

I built the Docker image for the application using the following command:

```sh
docker build -t zoomcamp-model:3.11.5-hw10 .
```

#### Step 4: Test the Docker Image Locally

To ensure the Docker image was built correctly, I ran the image locally and mapped port 9696 on my local machine to port 9696 in the container:

```sh
docker run -it --rm -p 9696:9696 zoomcamp-model:3.11.5-hw10
```

#### Step 5: Create a Kind Cluster

I created a Kind cluster to run the Kubernetes environment locally:

```sh
kind create cluster
```

#### Step 6: Verify Cluster Creation

I checked the services running in the cluster to ensure it was created successfully:

```sh
kubectl get services
```

#### Step 7: Load the Docker Image into Kind

I loaded the previously built Docker image into the Kind cluster:

```sh
kind load docker-image zoomcamp-model:3.11.5-hw10
```

#### Step 8: Apply the Deployment Configuration

I applied the deployment configuration to create the necessary pods:

```sh
kubectl apply -f deployment.yaml
```

#### Step 9: Verify Pod Creation

I checked the list of running pods to ensure the deployment was successful:

```sh
kubectl get pods
```

#### Step 10: Apply the Service Configuration

I applied the service configuration to expose the deployment:

```sh
kubectl apply -f service.yaml
```

#### Step 11: Verify Service Creation

I checked the list of services to ensure the service was created successfully:

```sh
kubectl get services
```

#### Step 12: Test the Service Locally

To test the service locally, I forwarded port 9696 on my local machine to port 80 on the service:

```sh
kubectl port-forward service/subscription-service 9696:80
```

Finally, I ran the `q6_test.py` script to verify that the service was working correctly and returned the expected results.
