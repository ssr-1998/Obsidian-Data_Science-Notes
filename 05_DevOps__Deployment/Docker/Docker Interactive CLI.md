## 🧭 Docker CLI Index

- [[#Verify Docker is Installed]]
- [[#Pull an Image from Docker Hub]]
- [[#List Available Docker Images]]
- [[#Run a Container (Interactive Mode)]]
- [[#Run a Container in the Background (Detached Mode)]]
	- [[#Is `sleep` Required in Detached Mode?]]
- [[#Accessing a Running Container in Detached Mode]]
- [[#Run a Container (One-off Commands without Interactive or Detached Modes)]]
- [[#List Running Containers]]
- [[#List Running all Containers (including Stopped)]]
- [[#Stop a Running Container]]
- [[#Start a Stopped Container]]
- [[#Remove a Container]]
- [[#Remove an Image]]
- [[#Build a Docker Image from a Dockerfile]]
- [[#Run Custom Image as a Container]]
- [[#View Logs of a Container]]
- [[#Access a Running Container's Shell]]
- [[#Clean Up Unused Docker Resources]]
- [[#To be Added]]
	- [[#Inspect a Container]]
	- [[#Create/Use Docker Volumes]]
	- [[#Manage Docker Networks]]
	- [[#Tag and Push Image to Docker Hub]]
	- [[#Copy files into/from Containers]]
	- [[#Restart a Container]]
	- [[#Export & Import Docker Images]]
	- [[#View Docker Disk Usage]]
	- [[#Remove All Containers/Images (Carefully)]]

## Verify Docker is Installed

Command
```bash
docker -v
```

Output
```bash
Docker version 28.1.1, build 4eba377
```

---
## Pull an Image from Docker Hub

Command
```bash
docker pull python:3.10
```

Output
```bash
3.10: Pulling from library/python
37f838b71c6b: Pull complete
87e918915732: Pull complete
ebed137c7c18: Pull complete
c2e76af9483f: Pull complete
873a4c802874: Pull complete
b3c901505532: Pull complete
6ce7a84f28e8: Pull complete
Digest: sha256:6ff000548a4fa34c1be02624836e75e212d4ead8227b4d4381c3ae998933a922
Status: Downloaded newer image for python:3.10
docker.io/library/python:3.10
```

---
## List Available Docker Images

Command
```bash
docker images
```

Output
```bash
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
python       3.10      6ff000548a4f   7 weeks ago   1.45GB
```

---
## Run a Container (Interactive Mode)

Command
```bash
docker run -it python:3.10
```

Output
```bash
Python 3.10.18 (main, Jul 22 2025, 04:26:07) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

- `-it`: interactive terminal.

- This starts the container **and gives you direct terminal access**.

- You can run Python interactively inside the container.

- It blocks your terminal until you exit the container (via `exit()` or `Ctrl+D`).

🟢 **Use case:** Development, debugging, exploring the container manually.

---
## Run a Container (Detached Mode - Background Running)

Command
```bash
docker run -d --name my-python-container python:3.10 sleep 3600
```

Output
```bash
810164b6bdc7e0f2c6099eca198dd8f09dc852406dc36...
```

- `-d` runs the container in the **background**.

- Your terminal is **freed up immediately**.

- But: you **don’t see any output or have direct access**.

- `Sleep 3600`: keeps the Container Running for an Hour.

🟢 **Use case:** Running long-lived services (e.g., Flask apps, web servers, databases).

### Is `sleep` Required in Detached Mode?

**No — not always.**

But:

- If the Container **has no long-running process**, like a Server or Background Job, **it will Exit Immediately** in Detached Mode.

- `sleep` is a placeholder command that keeps the Container alive for Testing.

In real use cases, we'd run something like:

```bash
docker run -d -p 5000:5000 my-flask-app
```

Which runs a Web Server that keeps the Container Alive.

---
## Accessing a Running Container in Detached Mode

Command
```bash
# To Access a Container Running in Detached Mode:
docker exec -it my-python-container bash

# Then run Python:
python
```

Output
```bash
# Output from 1st Command
root@810164b6bdc7:/#

# Output from 2nd Command
root@810164b6bdc7:/# python
Python 3.10.18 (main, Jul 22 2025, 04:26:07) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

---
## Run a Container (One-off Commands without Interactive or Detached Modes)

However, there are two Modes Primarily in Dockers to Run a Container i.e. **Interactive**, and **Detached**. But we can also **run One-off Commands without either** mode (useful for `Scripting` and `Automation`). By using:

```bash
docker run python:3.10 python -c "print('Hello from Docker')"
```

This is **neither Detached nor Interactive** — Docker runs the command, prints the output, and exits. We don't need `-it` or `-d`.

---
## List Running Containers

Command
```bash
docker ps
```

Output
```bash
CONTAINER ID   IMAGE         COMMAND       CREATED         STATUS         PORTS    

NAMES
--------------------------------------------------------------------------------

810164b6bdc7   python:3.10   "sleep 100"   9 seconds ago   Up 8 seconds            

my-python-container
```

---
## List Running all Containers (including Stopped):

Command
```bash
docker ps -a
```

Output
```bash
CONTAINER ID   IMAGE         COMMAND       CREATED          STATUS                 

PORTS     NAMES
--------------------------------------------------------------------------------

810164b6bdc7   python:3.10   "sleep 100"   25 seconds ago   Up 24 seconds
af2486adefaa   python:3.10   "python3"     5 minutes ago    Exited (0) 3 mins ago

		  my-python-container
          suspicious_thompson
```

---
## Stop a Running Container:

Command
```bash
docker stop my-python-container
```

Output
```bash
my-python-container
```

---
## Start a Stopped Container:

Command
```bash
docker start my-python-container
```

Output
```bash
my-python-container
```

---
## Remove a Container

Command
```bash
docker rm my-python-container
```

Output
```bash
my-python-container
```

- This command permanently removes a **stopped container**.

- You cannot remove a **running container** unless you stop it first.

---
## Remove an Image

Command
```bash
docker rmi python:3.10
```

Output
```bash
Untagged: python:3.10

Untagged: python@sha256:6ff000548a4fa34c1be02624836e75e212d4ead8227b4d4381c3ae998933a922

Deleted: sha256:6ff000548a4fa34c1be02624836e75e212d4ead8227b4d4381c3ae998933a922
```

- Use this to free disk space or remove outdated images.

- Make sure **no containers** are using the image.

---
## Build a Docker Image from a Dockerfile

Command
```bash
docker build -t my-flask-app .
```

Output
```bash
Sending build context to Docker daemon  3.072kB
Step 1/5 : FROM python:3.10-slim
 ---> 76a5a3c3c4d4
Step 2/5 : WORKDIR /app
 ---> Using cache
 ---> 2f3e5e40ab0c
Step 3/5 : COPY . .
 ---> Using cache
 ---> 763fdc6d0509
Step 4/5 : RUN pip install flask
 ---> Running in 45f3d0a5e693
Collecting flask
...
Successfully built 3a1f9c1edb42
Successfully tagged my-flask-app:latest

```

- Make sure your directory contains a `Dockerfile` and app source code.

---
## Run Custom Image as a Container

Command
```bash
docker run -d -p 5000:5000 my-flask-app
```

Output
```bash
3a1f9c1edb42aef8cd67d442e1234567a123bcde456fa567890b2cd34efab1234
```

- `-p 5000:5000` maps Host Port 5000 to Container Port 5000.

- Flask app should be accessible at `http://localhost:5000`.

---
## View Logs of a Container

Command
```bash
docker logs my-flask-app
```

Output
```bash
 * Serving Flask app 'app.py'
 * Running on http://0.0.0.0:5000 (Press CTRL+C to quit)
```

- Use this to debug or inspect container output.

---
## Access a Running Container's Shell

Command
```bash
docker exec -it my-flask-app /bin/bash
```

Output
```bash
root@3a1f9c1edb42:/app#
```

- You can explore the container file system or run commands manually.

---
## Clean Up Unused Docker Resources

Command
```bash
docker system prune -a
```

Output
```bash
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all images without at least one container associated with them
  - all build cache

Are you sure you want to continue? [y/N] y
Deleted Containers:
810164b6bdc7e0f2c6099eca198dd8f09dc852406dc36...

Deleted Images:
python:3.10

Total reclaimed space: 1.5GB
```

- Frees up disk space by removing unused data.

- ⚠️ Use with caution — it deletes a lot!

---
## To be Added:

### Inspect a Container

Command
```bash
docker inspect my-python-container
```

> Useful for checking all metadata like IP, volume mounts, etc.

### Create/Use Docker Volumes

Command
```bash
docker volume create my-volume
docker run -v my-volume:/data busybox
```

>Important for persistent data.

### Manage Docker Networks

Command
```bash
docker network ls
docker network inspect bridge
```

> Helps with container communication.

### Tag and Push Image to Docker Hub

Command
```bash
docker tag my-flask-app your-dockerhub-username/my-flask-app
docker push your-dockerhub-username/my-flask-app
```

> Essential for sharing images.

### Copy files into/from Containers

Command
```bash
docker cp myfile.txt my-container:/app/
docker cp my-container:/app/logs.txt .
```

> Very useful for dev/debugging.

### Restart a Container

Command
```bash
docker restart my-python-container
```

> Useful during dev/test cycles.

### Export & Import Docker Images

Command
```bash
docker save my-flask-app > app.tar
docker load < app.tar
```

> Good for offline transfer/sharing.

### View Docker Disk Usage

Command
```bash
docker system df
```

> Quickly see image/container/volume sizes.

### Remove All Containers/Images (Carefully)

Command
```bash
docker rm $(docker ps -aq)
docker rmi $(docker images -q)
```

> Powerful cleanup commands — include with ⚠️ warning.
