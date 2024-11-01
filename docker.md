# Introduction to Docker

Docker is an open-source platform designed to simplify and automate the deployment, scaling, and management of applications in lightweight, portable containers. Containers package up applications with all necessary dependencies, making them easy to run on any machine with Docker installed, regardless of the underlying environment.

## Key Concepts

- **Images**: Docker images are templates used to create containers. They include everything required to run an application, such as the OS, application code, libraries, and dependencies.
  
- **Containers**: Containers are runtime instances of Docker images. They provide a lightweight and isolated environment, allowing applications to run consistently across different platforms.

- **Dockerfile**: A Dockerfile is a text file with a series of commands for creating a Docker image. It specifies the environment in which the application will run, dependencies to install, and any configuration files needed.

- **Docker Compose**: Docker Compose is a tool for defining and running multi-container Docker applications using a single YAML configuration file (`docker-compose.yml`). This is useful for applications that require multiple services to run in tandem, like a web server, database, and cache.

---

# Instructions for Creating a Docker Container

## 1. Using a Dockerfile

The following steps outline how to create a Docker container from a Dockerfile.

### Step 1: Create a Dockerfile

Write a `Dockerfile` in the project directory. Here's an example `Dockerfile` for a simple deep-learning application:

```dockerfile

#Base Image
FROM python:3.7-slim

# Create and set the working directory
WORKDIR ./src

# Install the application dependencies
COPY requirements.txt .

RUN apt-get update
RUN apt install -y build-essential libpoppler-cpp-dev pkg-config python3-dev wget ffmpeg libsm6 libxext6 poppler-utils
RUN pip install --no-cache-dir -r requirements.txt


# Copy in the source code
COPY africa_poverty .
COPY test_model1.ipynb .
COPY clean_outputs.ipynb .

# Expose the application port
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
# RUN useradd app
# USER app

# Run the application
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

```

### Step 2: Build the Docker Image
Run the following command in the terminal to build the Docker image:

```
docker build -t name-prj .
```

### Step 3: Run the Docker Container
After building the image, run the container using:
```
docker run -p 3000:5000 my-node-app
```
This command starts the container and maps port 3000 of the host to port 5000 of the container, allowing you to access the app on localhost:3000.

To access a container, check the corresponding container using the `docker ps` command, then use this command: `docker exec -ti container_id bash`