# Table of Contents:
1. [[#Definition]]
2. [[#Functionalities]]
3. [[#Key Concepts]]
	1. [[#Containers]]
	2. [[#Docker Engine]]
		1. [[#Docker Daemon (`dockerd`)]]
			1. [[#Responsibilities]]
		2. [[#Docker CLI (`docker`)]]
			1. [[#Common Docker CLI Commands]]
			2. [[#Command Flow]]
	3. [[#Basic Docker Terminologies]]
	4. [[#Dockerfile Building an Image]]
	5. [[#Port Mapping]]
		1. [[#Real-World Analogy]]
		2. [[#Example]]
		3. [[#General Syntax Variations]]
			1. [[#1. `-p host_port container_port`]]
			2. [[#2. `-p ip host_port container_port`]]
			3. [[#3. `-P` (Capital P)]]
		4. [[#Dockerfile Hint — `EXPOSE`]]
		5. [[#Common Pitfalls]]
		6. [[#Diagnostic Commands]]
	6. [[#Docker Networking]]
		1. [[#Types of Docker Networks]]
		2. [[#Common Networking Commands]]
			1. [[#Example Connect two Containers via Custom Bridge]]
	7. [[#Docker Compose]]
		1. [[#Why Compose?]]
		2. [[#Sample `docker-compose.yml`]]
		3. [[#Useful Commands]]
	8. [[#Advanced Docker Topics]]
		1. [[#Security Best Practices]]
		2. [[#Health Checks]]
		3. [[#Docker Volumes (Data Persistence)]]
		4. [[#CI/CD with Docker]]
4. [[#Virtual Machine (VM)]]
	1. [[#Key Components of VM Architecture]]
5. [[#📊 VM vs Docker Visual Comparison]]
	1. [[#Stack Comparison]]
		1. [[#Traditional VM Stack]]
		2. [[#Docker Container Stack]]
	2. [[#⚔️ Comparison Table Docker vs VM]]
	3. [[#When to Use What?]]
	4. [[#🧠 Summary]]

# Definition:

- **Docker** is a tool that helps you **build, ship, and run applications inside containers**.

- It's a way to package an Application with all the necessary `Dependencies` and `Configurations`. Which, makes the Application a **Portable Artifact** (easy to share and can be moved to any Environment).

- Docker makes **Development & Deployment** more `easy` and `efficient`.

Imagine you're working on a project that works perfectly on your computer but doesn't work on someone else's. That’s the “it works on my machine” problem. Docker solves this by **packing your app with everything it needs to run — OS, libraries, dependencies — into a single container**.

# Functionalities:

| **Functionality**    | **Description**                                                            |
| -------------------- | -------------------------------------------------------------------------- |
| **Containerization** | Encapsulates application and its dependencies into a single portable unit. |
| **Isolation**        | Ensures separate environments for each container.                          |
| **Portability**      | “Write once, run anywhere” – same container works across all environments. |
| **Version Control**  | Images can be versioned and rolled back if needed.                         |
| **Efficiency**       | Shares OS kernel – less overhead than VMs.                                 |
| **Security**         | Isolated runtime and network environments.                                 |

# Key Concepts:
## Containers:

- A **container** is a **lightweight, standalone, executable package**.

- Its a Running Instance of an Image.

- It contains:
	- Application Code
	
	- Runtime (e.g., Python, SQL, Node.js, etc.)
	
	- System Tools & Libraries

- It **shares the Host OS Kernel**, making it much lighter than `Virtual Machines`.

**Analogy:**
Think of a container like a **shipped box** with all the parts your app needs to run.

## Docker Engine:

- **Docker Engine** is a software installed on your Machine that let's you build & run the Containers.

- It includes:
	- **Docker Daemon ( `dockerd` )** - brain that does all the heavy lifting & runs in the background.
	
	- **Docker CLI ( `CLI` )** - command-line tool to interact & control the Docker.
### Docker Daemon (`dockerd`):

- The **Docker Daemon** is the Background Service running on the `Host`.

- It manages all Docker Objects: **Containers, Images, Networks, and Volumes**.

- Listens for Docker API Requests (from `CLI` or `other apps`) and handles them.
#### Responsibilities:

- Building and Running the Containers.

- Managing Images and Volumes.

- Handling Container Lifecycle.

- Communicating with Docker Registry (like Docker Hub)

### Docker CLI (`docker`):

- **Docker CLI** is the Command-Line Tool used to **Interact with the Docker**.

- We use it to Send Commands to the `Docker Daemon`.
#### Common Docker CLI Commands:
| **Command**                      | **What it Does**                          |
| -------------------------------- | ----------------------------------------- |
| **docker build -t myapp .**      | Builds an Image from Dockerfile           |
| **docker images**                | Lists Images                              |
| **docker run myapp**             | Runs a Container from an Image            |
| **docker ps**                    | Lists Running Containers                  |
| **docker ps -a**                 | Lists all Containers                      |
| **docker exec myapp ls -l /app** | Runs a command inside a running Container |
| **docker stop <container_id>**   | Stops a Container                         |
| **docker rm <container_id>**     | Removes a Container                       |
| **docker rmi <image_id>**        | Removes an Image                          |

For a detailed walkthrough about all the CLI Commands, check [[Docker Interactive CLI]]

#### Command Flow:

![[Docker_Command_Execution_Flow.png]]

---
## Basic Docker Terminologies:

| Term             | Meaning                                               |
| ---------------- | ----------------------------------------------------- |
| **Image**        | A read-only blueprint for Containers (like a recipe)  |
| **Dockerfile**   | A text file with instructions to build a Docker Image |
| **Docker Hub**   | A Public Repository of Docker Images                  |
| **Volume**       | Used to persist Data Outside Containers               |
| **Port Mapping** | Maps Container Ports to Host Machine Ports            |

---
## Dockerfile: Building an Image

A `Dockerfile` is a Script of Instructions to build a **Docker Image**.

**Example Dockerfile:**

```dockerfile
# Base image
FROM python:3.10

# Maintainer info
LABEL maintainer="you@example.com"

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Define environment variables
ENV DEBUG=True

# Expose port
EXPOSE 5000

# Command to run container
CMD ["python", "app.py"]
```

---
## Port Mapping:

Port Mapping is the process of connecting a **port on your host machine** (e.g., your laptop or server) to a **port inside a Docker container**.

**Syntax:**
```bash
docker run -p <host_port>:<container_port> <image_name>
```
### Real-World Analogy:

Think of your Docker Container like a **Restaurant Kitchen** (hidden behind the walls), and Port Mapping is the **Window where Waiters pick up the Food** (a way to expose Internal Services to the Outside).

Without it, your app is running, but you have no way to reach it.
### Example

Suppose you have a Flask app running inside a container on port **5000**.

```bash
docker run -d -p 5000:5000 flask_app
```

**What it means:**

- **Inside the container:** Your Flask App is listening on **Port 5000**

- **Outside the container (host):** You Expose that Internal Port as **Port 5000**

- → Now, `http://localhost:5000` works in your Browser.
### General Syntax Variations:

#### 1. `-p host_port:container_port`

Maps a specific **host** port to a **container** port.

```bash
docker run -p 8080:80 nginx
```

- Access Nginx via `localhost:8080`

- Inside container, it runs on port 80
#### 2. `-p ip:host_port:container_port`

Binds the port to a specific **host IP address**.

```bash
docker run -p 127.0.0.1:8080:80 nginx
```

- Accessible only via `localhost:8080`, **not from other machines**
#### 3. `-P` (Capital P)

**Automatically maps all exposed ports** in the Dockerfile to **random host ports**.

```bash
docker run -P nginx
```

- Maps Port 80 inside the Container to something like Host Port 49153.

- Use `docker port <container_id>` to see Mapping.
### Dockerfile Hint — `EXPOSE`

You can declare which ports the container **might expose** by writing:

```dockerfile
EXPOSE 5000
```

But this doesn't actually publish the port — it's just **metadata**. You still need `-p` or `-P` during `docker run`.
### Common Pitfalls:

| Problem                        | Cause                              | Fix                                  |
| ------------------------------ | ---------------------------------- | ------------------------------------ |
| `localhost refused to connect` | App listening on `127.0.0.1`       | Change to `0.0.0.0` inside container |
| App not accessible externally  | Didn’t map port                    | Use `-p` or check firewall           |
| Port already in use            | Another service uses the host port | Use a different `host_port` in `-p`  |
| `-P` maps to random ports      | You expected specific ones         | Use `-p` for deterministic mapping   |

### Diagnostic Commands:

```bash
docker ps                         # See mapped ports

docker port <container_id>       # Show port mapping

docker inspect <container>       # Deep config info
```

---
## Docker Networking:

Docker networking enables containers to communicate with each other, the host, and the outside world.
### Types of Docker Networks:

| **Network Type**       | **Description**                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| **bridge** _(default)_ | Used for `container-to-container` communication on the same Host. Each container gets a Private IP. |
| **host**               | Container shares the Host’s Network Stack. No Isolation. Faster, but less Secure.                   |
| **none**               | Disables all Networking. Isolated Container.                                                        |
| **overlay**            | Enables multi-host Container Communication (requires `Docker Swarm or Kubernetes`).                 |
| **macvlan**            | Assigns MAC Addresses to Containers.<br>Containers appear as Physical Devices on the Network.       |

### Common Networking Commands:

```bash
docker network ls                        # List all networks

docker network inspect <network>        # Inspect a network

docker network create --driver bridge my_bridge_net

docker run --network=my_bridge_net ...
```

#### Example: Connect two Containers via Custom Bridge

```bash
docker network create my_net

docker run -dit --name app1 --network my_net python:3.10

docker run -dit --name app2 --network my_net ubuntu
```

## Docker Compose:

**Docker Compose** is a tool for defining and managing multi-container Docker applications using a `docker-compose.yml` file.
### Why Compose?

- Declarative syntax for building Services, Networks, and Volumes.

- One-command Orchestration: `docker-compose up`
### Sample: `docker-compose.yml`

```yaml
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - redis
  redis:
    image: "redis:alpine"

```

### Useful Commands:

```bash
docker-compose up           # Start services

docker-compose up -d        # Detached mode

docker-compose down         # Stop and clean

docker-compose ps           # List running services

docker-compose logs         # View logs
```

## Advanced Docker Topics:

### Security Best Practices:

- Use **Minimal Base Images** (e.g., `alpine`, `distroless`) to reduce attack surface.

- Run Containers as **non-root users**.

- Use **Docker Bench for Security** to Audit Containers.

- Use **Secrets Management** (e.g., `Docker Secrets`, `Vault`).

### Health Checks:

Define container health logic inside Dockerfile.

```dockerfile
HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost:5000/health || exit 1
```

### Docker Volumes (Data Persistence):

Used to store Data outside the Container Lifecycle.

```bash
docker volume create mydata

docker run -v mydata:/app/data ...
```

### CI/CD with Docker

- Use Docker in **CI Pipelines** (`GitHub Actions`, `GitLab CI`, `Jenkins`).

- **Common Steps:** `Build Image` → `Run tests` → `Push to Docker Hub` → `Deploy`

# Virtual Machine (VM)

A **Virtual Machine (VM)** is like a **computer inside your computer**. It acts like a real physical machine, running its own full operating system and the apps you install on it — just like a regular computer.

## Key Components of VM Architecture:

```scss
Hardware (Physical Server)
     └── Host OS (e.g., Windows, Linux)
         └── Hypervisor (Type 1 or Type 2)
             ├── VM 1
             │    ├── Guest OS (e.g., Ubuntu)
             │    └── App + Dependencies
             ├── VM 2
             │    ├── Guest OS (e.g., CentOS)
             │    └── App + Dependencies
             └── VM N
```

- **Hardware (Physical Server):**

	- The Actual Machine (CPU, RAM, Storage) that runs everything.

- **Host OS:**

	- The Operating System installed directly on the Physical Server.
	
	- Examples: Windows, Linux.

- **Hypervisor:**

	- Software that Creates and Manages Virtual Machines.
	
	- Two types:
	
		- **Type 1 (Bare-metal):** Runs directly on the hardware, e.g., `VMware ESXi`, `Xen`.
		
		- **Type 2:** Runs on top of the Host OS like a Regular Application, e.g., `VirtualBox`, `VMware Workstation`.

- **Virtual Machines (VMs):**

	- Each VM behaves like a separate Computer.
	
	- Contains:
	
		- **Guest OS:** The Operating System inside the VM (e.g., Ubuntu, CentOS).
		
		- **Application + Dependencies:** Software and all it needs to run.

- **VM1, VM2, ..., VM N:**

	- Multiple VMs can run on the same Hardware, each Isolated with its own OS and Apps.

# 📊 VM vs Docker: Visual Comparison

## Stack Comparison:

### Traditional VM Stack:

```scss
[Hardware]
    └── Host OS
        └── Hypervisor
            ├── VM1
            │    ├── Guest OS (Linux)
            │    └── App A + Libraries
            ├── VM2
            │    ├── Guest OS (Windows)
            │    └── App B + Libraries
```

🟡 **Each VM has its own OS**, which consumes more memory and CPU.

### Docker Container Stack:

```scss
[Hardware]
    └── Host OS (Linux/Windows)
        └── Docker Engine
            ├── Container 1
            │    └── App A + Libraries
            ├── Container 2
            │    └── App B + Libraries
```

🟢 **All containers share the host OS kernel**, making them lightweight and faster to start.

## ⚔️ Comparison Table: Docker vs VM

| **Feature**            | **Docker Containers**                  | **Virtual Machines**                    |
| ---------------------- | -------------------------------------- | --------------------------------------- |
| **OS Virtualization**  | No (shares host kernel)                | Yes (each VM has full OS)               |
| **Startup Time**       | Seconds                                | Minutes                                 |
| **Resource Usage**     | Low (no OS overhead)                   | High (runs full OS per VM)              |
| **Size**               | MBs                                    | GBs                                     |
| **Portability**        | High (run anywhere with Docker)        | Moderate (dependent on hypervisor)      |
| **Isolation**          | Process-level                          | Full OS-level                           |
| **Security**           | Moderate (shared kernel)               | High (OS isolation)                     |
| **Performance**        | Near-native                            | Slower due to hypervisor                |
| **Management Tooling** | Docker CLI, Compose, Swarm, Kubernetes | VMware, VirtualBox, vSphere, etc.       |
| **Use Cases**          | Microservices, DevOps, CI/CD           | Legacy systems, GUI apps, full desktops |

## When to Use What?

| **Scenario**                                | **Recommended** |
| ------------------------------------------- | --------------- |
| **You need full OS access per application** | VM              |
| **You want lightweight, fast deployments**  | Docker          |
| **Running Apps with different OS needs**    | VM              |
| **Running Microservices or APIs**			  | Docker          |
| **Full system-level isolation needed**      | VM              |
| **Microservices, CI/CD Pipelines**          | Docker          |
| **GUI apps and OS-dependent tools**         | VM              |

## 🧠 Summary:

- **VMs are better for OS-level Isolation and Legacy apps.**

- **Docker is ideal for Cloud-Native, Scalable, Lightweight, and Portable Applications.**

- Docker Containers are **~10x faster and lighter** than VMs, but **VMs** offer better **isolation and compatibility**.
