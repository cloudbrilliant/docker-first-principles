# ⚗️ Docker First Principles

Docker is a powerful tool for creating consistent, isolated, and portable development environments.

- 🗃️ Why use Docker? You seek: Consistency, Isolation, Reproducibility, Portability, Scalability, Efficiency, Speed & Parity
- 💡 When to use Docker? When one or more of the above is important
- 📝 How to use Docker? That's why you're here 🙈

## Getting Started

- Check Docker is installed/running or install Docker <https://docs.docker.com/engine/install/>
- Clone this repo `gh repo clone cloudbrilliant/docker-first-principles`
- Open docker-first-principles in VSCode, Cursor or something else

## Concepts

Docker is configured and managed using the following `Dockerfile`, `docker-compose.yaml`
and `.dockerignore`

- Dockerfile

  - Defines how to build a single Docker image
  - Specifies the base image, environment, files to add, commands to run, and other configuration for a single container
  - Used with the docker build command to create an image

- docker-compose.yaml

  - Defines and manages single to multi-container Docker applications
  - Specifies services, networks, and volumes for a complete application stack
  - Allows you to configure relationships between containers
  - Used with the `docker compose` command to manage containers as a single service

- Summary: `Dockerfile` and `docker-compose.yaml` builds images, `docker-compose.yaml` orchestrates containers

## Basic Docker Usage

Open the terminal in VSCode (or your preferred method) and run the following commands one at a time to create a Python 3.12 environment. This setup gives your current folder access as a volume, allowing you to modify files in your IDE while executing terminal commands within the running container.

### Docker Compose Up - Fire up the container 🔥

```bash
docker compose up -d
```

### Docker Compose Exec - Run stuff in the container 🚀

```bash
docker compose exec app bash
```

- Allows you to execute an interactive bash shell inside a running container named "app"
- Useful for debugging, running commands, or inspecting the container's environment
- docker compose exec: This is the command to execute a command in a running container
- app: This is the name of the service (as defined in your docker-compose.yaml file) you want to access
- bash: This is the command you want to run inside the container (in this case, starting a bash shell).

### Docker Down - When done 🗑️

```bash
docker compose down
```

- Clean way to shut down your Docker environment
- Doesn't remove the images used by the containers

### Docker Down All ⚰️

```bash
docker compose down --rmi all --volumes
```

This command is a more thorough version of docker compose down. It not only stops and removes containers, networks, and volumes, but also:

- `--rmi all`: Removes all images used by the services defined in the docker-compose.yaml file.
- `--volumes`: Removes named volumes defined in the volumes section of the docker-compose file and anonymous volumes attached to containers.

This command is useful when you want to completely clean up your Docker environment, including images and persistent data stored in volumes. *Be cautious when using this command as it will delete data stored in volumes.*

## Official Python Docker Images

Before you ask about the difference in Python Docker Images - here you go

<https://hub.docker.com/_/python/>

- Slim Buster: Built on the widely used Debian Buster, Slim Buster boasts excellent compatibility with most Python libraries. You’re less likely to encounter unexpected compatibility issues here.

- Alpine: While smaller, Alpine’s reliance on musl libc can lead to compatibility issues with libraries heavily dependent on the standard glibc found in most other Linux distributions. Be prepared for troubleshooting potential conflicts.

- Slim Bullseye: Occupying a middle ground, Slim Bullseye offers better compatibility than Alpine due to its Debian base but might still face occasional issues with libraries specifically requiring older glibc versions.

## Some Python Frameworks to try out

Here are some frameworks picked for simplicty, easy to learn and great documentation.

- mirascope <https://docs.mirascope.io/latest/>
- fasthtml <https://docs.fastht.ml/>
- fastapi <https://fastapi.tiangolo.com/>
- openai <https://platform.openai.com/docs/introduction>

These are installed automatically in your container - checkout the `requirements.txt` file

Run `docker compose up -d` then `docker compose exec app bash` to get started

### Chat with AI

Obtain an Open API Key from <https://platform.openai.com/account/api-keys>

Try this

- `export OPENAI_API_KEY='YOUR KEY HERE'`
- `python src/main_ai.py`
- Ask some questions

### Create an API

Try this

- `python src/main_api.py`
- Open `http://0.0.0.0:5002` in your browser or postman (get request)
- Try this `http://0.0.0.0:5002/items/1`

### Create a Web App

Try this

- `python src/main_web.py`
- Open `http://0.0.0.0:5001` in your browser
- Click the text
