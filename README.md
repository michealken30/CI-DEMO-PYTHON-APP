# Hello Python — Docker + GitHub Actions Starter

A minimal Python app that prints **Hello**. Includes unit tests, a Dockerfile, and a CI workflow that tests, builds, and pushes to Docker Hub.

---

## Features

- 🐍 Simple Python entrypoint (`app/main.py`)
- ✅ Pytest-based unit test
- 🐳 Dockerfile (Python 3.12 slim)
- 🤖 GitHub Actions workflow: **test → build → push**

---

## Prerequisites

- Python 3.12 (for local testing) — optional
- Docker
- GitHub repo connected to this project
- Docker Hub account

---

## Run Locally (no Docker)

```bash
python -m app.main
# Output: Hello

python -m pip install --upgrade pip
pip install pytest
pytest -q

docker build -t hello-python:dev .

# Run the container
docker run --rm hello-python:dev

# Log in once
docker login

# Tag and push
DOCKERHUB_USERNAME=yourname
IMAGE_NAME=hello-python

docker tag hello-python:dev docker.io/$DOCKERHUB_USERNAME/$IMAGE_NAME:latest
docker push docker.io/$DOCKERHUB_USERNAME/$IMAGE_NAME:latest

CI/CD with GitHub Actions

This repo includes .github/workflows/ci.yml which:

Tests the code on every push/PR (Python 3.12, pytest).

Builds the Docker image on pushes to branches/tags.

Pushes images to Docker Hub on pushes (not PRs).

Required GitHub Secrets

DOCKERHUB_USERNAME — your Docker Hub username

DOCKERHUB_TOKEN — Docker Hub access token (Account Settings → Security → New Access Token)

(optional) IMAGE_NAME — defaults to hello-python if not set

Image Tags Produced

:sha-<shortsha> (e.g., sha-abc1234)

:<branch> for branch pushes (e.g., main)

:latest when pushing the default branch

Tags from Git tags (e.g., push v1.2.3 → tag 1.2.3)

Resulting image name: docker.io/$DOCKERHUB_USERNAME/$IMAGE_NAME:<tag>



Project Structure


app/            # application code
  main.py       # prints "Hello"
  __init__.py   # package marker

.tests/         # unit tests
.github/workflows/ci.yml   # CI pipeline
Dockerfile      # Docker build recipe
.dockerignore   # exclude files from build context
requirements.txt
README.md
```
