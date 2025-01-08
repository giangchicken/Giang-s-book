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
For more information abt the difference bw dockerfile and docker-compose [dockerfile_docker-compose](https://viblo.asia/p/docker-vs-docker-compose-RnB5pXGd5PG)

---

# Instructions for Creating a Docker Container

## 1. Using a Dockerfile

The following steps outline how to create a Docker container from a Dockerfile.

### Step 1: Create a Dockerfile

Write a `Dockerfile` in the project directory. Here's an example `Dockerfile` for a simple deep-learning application:

```bash

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

```bash
docker build -t name-prj .
```

### Step 3: Run the Docker Container
After building the image, run the container using:
```bash
docker run -p 3000:5000 name-prj
```
This command starts the container and maps port 3000 of the host to port 5000 of the container, allowing you to access the app on localhost:3000.

To access a container, check the corresponding container using the `docker ps` command, then use this command: `docker exec -ti container_id bash`

---

## 2. Using a docker-compose

### Step 1: Write a `Dockerfile`

Before creating a docker-compose.yml file, you must have a functional Dockerfile (see the example in the previous section).

### Step 2: Create a `docker-compose.yml` File

Below is an example docker-compose.yml file for orchestrating a JupyterLab container:

```bash
version: '3'

services:
  jupyterlab:
    build:
      context: .
      dockerfile: dockerfile
    ports:
      - "8080:8888"  # Map local port 8080 to container port 8888
    volumes:
      - ./data_quanhuyen:/data_quanhuyen
      - ./data_xaphuong:/data_xaphuong
      - ./data_tinh:/data_tinh
      - ./features_xaphuong:/features_xaphuong
      - ./features_quanhuyen:/features_quanhuyen
      - ./features_tinh:/features_tinh
    environment:
      - JUPYTER_ENABLE_LAB=yes  # Enable JupyterLab
    command: jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root

```

### Step 3: Build and Run the Containers Using `docker-compose`

Build the services: Run the following command to build the services defined in the docker-compose.yml file:
```bash
docker-compose build
```

Start the containers: Use this command to run the containers:

```bash
docker-compose up
```

Stop the containers: To stop the running containers, use:
```bash
docker-compose down
```

Run in detached mode: If you want to run the containers in the background (detached mode), use:

```bash
docker-compose up -d
```
---
# **Docker Engine**

Docker supports the following types
---
## **Storage**

Data written to the container layer doesn't persist when the container is destroyed. This means that it can be difficult to get the data out of the container if another process needs it.

Docker supports the following types of storage mounts for storing data outside of the writable layer of the container: `Volume mounts`, `Bind mounts`, `tmpfs mounts`, `Named pipes`

| Types  | Usage |
|------|-----------|
| Volume mounts  |    Volumes are persistent storage mechanisms managed by the Docker daemon. They retain data even after the containers using them are removed. Volume data is stored on the filesystem on the host, but in order to interact with the data in the volume, you must mount the volume to a container. Directly accessing or interacting with the volume data is unsupported, undefined behavior, and may result in the volume or its data breaking in unexpected ways.    |
| Bind mounts  |    Bind mounts create a direct link between a host system path and a container, allowing access to files or directories stored anywhere on the host. Since they aren't isolated by Docker, both non-Docker processes on the host and container processes can modify the mounted files simultaneously.    |
| tmpfs mounts  |    A tmpfs mount stores files directly in the host machine's memory, ensuring the data is not written to disk. This storage is ephemeral: the data is lost when the container is stopped or restarted, or when the host is rebooted. tmpfs mounts do not persist data either on the Docker host or within the container's filesystem.    |
| Named pipes   |    Named pipes can be used for communication between the Docker host and a container. Common use case is to run a third-party tool inside of a container and connect to the Docker Engine API using a named pipe    |

---
## **Volumes**


---
# Docker Commands Overview

## Docker Management Commands
- **`docker --version`**  
  Displays the installed Docker version.

- **`docker info`**  
  Provides detailed information about Docker, including system status, number of containers, images, etc.

- **`docker help`**  
  Lists available Docker commands and their descriptions.

## Container Lifecycle Commands
- **`docker run [options] image`**  
  Creates and starts a new container from the specified image.
  
- **`docker start container_id`**  
  Starts an existing, stopped container.

- **`docker stop container_id`**  
  Stops a running container gracefully.

- **`docker restart container_id`**  
  Stops and then restarts a container.

- **`docker kill container_id`**  
  Forcefully stops a running container.

- **`docker rm container_id`**  
  Removes a stopped container.

- **`docker ps`**  
  Lists currently running containers.

- **`docker ps -a`**  
  Lists all containers, including stopped ones.

- **`docker logs container_id`**  
  Fetches and displays logs of a container.

- **`docker exec -it container_id command`**  
  Executes a command inside a running container (e.g., opening a bash shell).

## Image Management Commands
- **`docker pull image`**  
  Downloads an image from a Docker registry (e.g., Docker Hub).

- **`docker build -t image_name .`**  
  Builds an image from a Dockerfile in the current directory, tagging it with a name.

- **`docker push image_name`**  
  Uploads a locally tagged image to a Docker registry.

- **`docker images`**  
  Lists all local Docker images.

- **`docker rmi image_id`**  
  Deletes a specific Docker image from the local system.

- **`docker tag source_image target_image`**  
  Tags an image with a new name.

## Volume Commands
- **`docker volume create volume_name`**  
  Creates a new named volume for persistent data storage.

- **`docker volume ls`**  
  Lists all Docker volumes on the system.

- **`docker volume rm volume_name`**  
  Removes a specific volume.

## Network Commands
- **`docker network create network_name`**  
  Creates a custom network for Docker containers.

- **`docker network ls`**  
  Lists all Docker networks on the system.

- **`docker network connect network_name container_id`**  
  Connects a container to a specific network.

- **`docker network disconnect network_name container_id`**  
  Disconnects a container from a network.

## Docker Compose Commands
- **`docker-compose up`**  
  Creates and starts containers defined in a `docker-compose.yml` file.

- **`docker-compose down`**  
  Stops and removes containers, networks, volumes, and images created by `docker-compose up`.

- **`docker-compose build`**  
  Builds or rebuilds services defined in `docker-compose.yml`.

- **`docker-compose ps`**  
  Lists containers managed by the `docker-compose.yml` file.

- **`docker-compose logs`**  
  Displays logs for all containers managed by Docker Compose.

- **`docker-compose stop`**  
  Stops running containers without removing them.

- **`docker-compose start`**  
  Starts containers that have been stopped.

## Dockerfile Instructions
- **`FROM base_image`**  
  Specifies the base image for building a new image.

- **`RUN command`**  
  Executes a command during the image building process.

- **`COPY source destination`**  
  Copies files or directories from the host into the container.

- **`WORKDIR path`**  
  Sets the working directory within the container.

- **`CMD ["executable", "param1", "param2"]`**  
  Specifies the default command to run when the container starts.

- **`ENTRYPOINT ["executable", "param1", "param2"]`**  
  Configures a container to run as an executable.

- **`ENV key=value`**  
  Sets environment variables inside the container.

- **`EXPOSE port`**  
  Declares network ports the container will use.

## System Management Commands
- **`docker system df`**  
  Shows disk usage of Docker images, containers, and volumes.

- **`docker system prune`**  
  Removes all stopped containers, unused networks, and dangling images to free up space.

- **`docker stats`**  
  Shows real-time resource usage statistics for running containers.

## Additional Useful Commands
- **`docker inspect container_id`**  
  Retrieves detailed information about a container's configuration and status.

- **`docker history image`**  
  Shows the history of an image, listing each layer and its command.

- **`docker save -o file.tar image`**  
  Saves an image to a file, enabling it to be transferred and loaded elsewhere.

- **`docker load -i file.tar`**  
  Loads an image from a saved file into Docker.

- **`docker cp src_path container_id:dst_path`**  
  Copy file/folder from local to container.


---

# Hướng dẫn: Cho phép user sử dụng Docker mà không cần `sudo`

Dưới đây là các bước chi tiết để cho phép user sử dụng Docker mà không cần quyền `sudo`.

---

## **1. Kiểm tra nhóm `docker` đã tồn tại hay chưa**
Trên hầu hết các hệ thống, khi Docker được cài đặt, nhóm `docker` sẽ tự động được tạo ra. Để kiểm tra, chạy lệnh sau:

```bash
getent group docker
```
Nếu nhóm docker đã tồn tại, bạn sẽ thấy một dòng như sau:

```bash
docker:x:999:
```
Nếu không, tạo nhóm này bằng lệnh:

```bash
sudo groupadd docker
```

## **2. Thêm user vào nhóm `docker`**

Thêm user của bạn vào nhóm `docker` bằng lệnh:

```bash
sudo usermod -aG docker <username>
#Thay <username> bằng tên của user bạn muốn cấp quyền.
#Nếu muốn thêm user hiện tại của bạn, thay <username> bằng $(whoami).
```

## **3. Kiểm tra thay đổi**

Để thay đổi có hiệu lực:

- Đăng xuất và đăng nhập lại user.
- Hoặc chạy lệnh sau để áp dụng ngay mà không cần đăng xuất: 
```bash
  newgrp docker
```

## **4.Lưu ý quan trọng**
Quyền hạn của nhóm docker:
- Khi một user thuộc nhóm docker, họ có quyền kiểm soát toàn bộ hệ thống thông qua Docker (ví dụ: chạy container với quyền root). Hãy cân nhắc khi thêm user vào nhóm này.
- Nếu bạn quản lý một máy chủ dùng chung, hãy hạn chế quyền này hoặc sử dụng giải pháp thay thế như sudo docker kèm chính sách.

Để kiểm tra xem user đã thuộc nhóm docker chưa:
```bash
  groups <username>
```

Nếu muốn gỡ một user khỏi nhóm docker, chạy lệnh:
```bash
  sudo gpasswd -d <username> docker
```


---

# Docker Multi-stage builds

[Tutorial](https://pythonspeed.com/articles/smaller-python-docker-images/)
