
> Linked from [[🐳Dockers#Docker Compose]] — **Practical Demo of Docker Compose Project**
# Table of Contents:
- [[#📌 Agenda]]
- [[#📂 Project Structure]]
- [[#📦 Required Files for the Project]]
- [[#🔧 `docker-compose.yml` Key Concepts]]
- [[#🩺 Healthchecks in Docker Compose]]
- [[#🚀 Running the Project]]
- [[#✅ Testing the Flask App with Postman]]
	- [[#🔹 Request 1]]
	- [[#🔹 Request 2]]
	- [[#🔹 Request 3]]
	- [[#🔹 Request 4]]
- [[#📤 Stopping and Cleaning Up]]
- [[#🐳 Pushing the Flask Image to Docker Hub]]
- [[#📥 Using the Image from Docker Hub]]

## 📌 Agenda

This note covers a hands-on Docker Compose Project that runs a **Flask app**, a **MySQL database**, and **Redis** cache — all coordinated using a `docker-compose.yml` file. It demonstrates **container orchestration** and **service linking** through a **Practical Micro-Demo**.

## 📂 Project Structure

```mathematica
Docker-Compose/
├── docker-compose.yml
└── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
```

## 📦 Required Files for the Project

This project includes:

- A **Flask-based Python app** (`app.py`) that provides User APIs.

- `requirements.txt` listing Python dependencies.

- A `Dockerfile` to containerize the Flask App.

- The main orchestrator: `docker-compose.yml`.

> 📌 _Only the `docker-compose.yml` is discussed in detail here._

## 🔧 `docker-compose.yml` Key Concepts

Here's what this file defines:

- **Three services**:
	- `web`: Flask application
	
	- `db`: MySQL database
	
	- `redis`: Redis cache

- **Container names** for easy reference

- **Environment variables** for configuration (like DB credentials)

- **Port mapping** from host to container

- **Service dependencies**: Ensures DB and Redis start before the Flask app

**Key fields:**
```yaml
services:      # Defines each container/service
  web:
    build:     # Context to build the image from Dockerfile
    ports:     # Maps container port to host port
    depends_on:# Ensures dependent services start first
    environment:
      - MYSQL_HOST=db
      - REDIS_HOST=redis
```

## 🩺 Healthchecks in Docker Compose

Healthchecks ensure a container is not just **running**, but actually **ready** to serve requests.  
This prevents dependent services (like Flask) from starting too early.
### 🐬 MySQL Healthcheck
```yaml
healthcheck:
  test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
  interval: 5s
  timeout: 5s
  retries: 10
```

- Checks if MySQL server is accepting connections (`mysqld is alive`)

- Waits for up to 10 attempts with 5-second intervals
### 🟥 Redis Healthcheck
```yaml
healthcheck:
  test: ["CMD", "redis-cli", "ping"]
  interval: 5s
  timeout: 3s
  retries: 5
```
- Waits for Redis to respond with `PONG`
### 📌 Usage in `depends_on`
```yaml
depends_on:
  db:
    condition: service_healthy
  redis:
    condition: service_healthy
```

- Ensures Flask starts **only after** DB & Redis are healthy

🧠 **Tip:** Use `healthchecks` for all critical dependencies to avoid race conditions during container startup.
___
## 🚀 Running the Project

> ⚠️ Always run Docker commands **from the folder where `docker-compose.yml` is located**.

🔸 To start the App and Build Images:
```bash
docker-compose up --build
```

🔸 To start it without Rebuilding:
```bash
docker-compose up
```

🔸 To run in Detached Mode (background):
```bash
docker-compose up -d
```

___
## ✅ Testing the Flask App with Postman

Once the containers are up, test the app using **Postman**.
### 🔹 Request 1

**GET** → `http://127.0.0.1:5000/users`

**Output:**
```json
{
    "source": "db",
    "users": []
}
```

### 🔹 Request 2

**POST** → `http://127.0.0.1:5000/users`

**Body** (JSON):
```json
{
    "name": "User_1",
    "email": "user1@gmail.com"
}
```

**Output:**
```json
{
    "message": "User added successfully"
}
```

### 🔹 Request 3

**POST** → `http://127.0.0.1:5000/users`

**Body** (JSON):
```json
{
    "name": "User_2",
    "email": "user2@gmail.com"
}
```

**Output:**
```json
{
    "message": "User added successfully"
}
```

### 🔹 Request 4

**GET** → `http://127.0.0.1:5000/users`  

**Output:**
```json
{
    "source": "db",
    "users": [
        {
            "id": 1,
            "name": "User_1",
            "email": "user1@gmail.com"
        },
        {
            "id": 2,
            "name": "User_2",
            "email": "user2@gmail.com"
        }
    ]
}
```

---
## 📤 Stopping and Cleaning Up:

🔸 Gracefully stop containers:
```bash
docker-compose stop
```

🔸 Stop and remove containers:
```bash
docker-compose down
```

🔸 To remove volumes (including database data):
```bash
docker-compose down -v
```

---
## 🐳 Pushing the Flask Image to Docker Hub

1. Tag the Image:
```bash
docker tag flask-app-container yourdockerhubusername/flask-app:latest
```

2. Push the Image:
```bash
docker push yourdockerhubusername/flask-app:latest
```

---
## 📥 Using the Image from Docker Hub

Once the image is pushed, we can modify the `docker-compose.yml` as follows:
```yaml
services:
  web:
    image: yourdockerhubusername/flask-app:latest  # Change applied
    container_name: flask-app-docker_compose
    ports:
      - "5000:5000"
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      - MYSQL_HOST=db
      - MYSQL_USER=root
      - MYSQL_PASSWORD=secret
      - MYSQL_DB=flaskdb
      - REDIS_HOST=redis

  db:
    image: mysql:8.0
    container_name: mysql-db-docker_compose
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: flaskdb
    ports:
      - "3307:3306"
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 5s
      timeout: 5s
      retries: 10

  redis:
    image: redis:alpine
    container_name: redis-cache-docker_compose
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

```

> Can also use `ssr1998/flask-app-docker_compose:latest`, instead of making a new one.

Now, any user cloning your Compose project can simply run:
```bash
docker-compose up
```
…and the image will be **pulled from Docker Hub** — no need for source code or build context.

