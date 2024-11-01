# Docker Overview
Docker is an open platform for building, shipping, and running applications within isolated environments called **containers**. Containers allow developers to package applications with their dependencies, ensuring consistent behavior across environments and making deployment fast and efficient.

## Key Components of Docker

- **Docker Engine**: The underlying technology that runs and manages Docker containers.
- **Docker Daemon (dockerd)**: The server that builds, runs, and manages containers. It listens to Docker API requests and manages Docker objects (images, containers, volumes, etc.).
- **Docker Client (docker)**: The command-line interface used to interact with the Docker Daemon through commands (e.g., `docker run`, `docker pull`).
- **Docker Hub and Registries**: Docker Hub is the default public repository for storing images. You can also use private registries for custom images.
- **Docker Images**: Read-only templates used to create containers. Images can be based on a base image (e.g., Ubuntu) with added configurations or applications.
- **Docker Containers**: Runnable instances of Docker images. Containers are lightweight, isolated, and run as separate processes on the host OS. They can be started, stopped, moved, or deleted as needed.

## Docker Workflow
1. **Develop**: Use Docker containers to create and test applications in a consistent environment.
2. **Ship**: Share Docker images via Docker Hub or private registries.
3. **Deploy**: Deploy the application as a container to production, whether on a local server, cloud, or hybrid setup.

## Dockerfile
A **Dockerfile** is a script with instructions to create a Docker image. Each command in a Dockerfile adds a layer to the image, allowing for efficient updates by rebuilding only modified layers.

**Docker Compose** is a tool that allows you to define and manage multi-container Docker applications using a single YAML file, simplifying deployment and service connections.

For more information [docker docs](https://docs.docker.com/get-started/docker-overview/)

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
docker run -p 3000:5000 name-prj
```
This command starts the container and maps port 3000 of the host to port 5000 of the container, allowing you to access the app on localhost:3000.

To access a container, check the corresponding container using the `docker ps` command, then use this command: `docker exec -ti container_id bash`