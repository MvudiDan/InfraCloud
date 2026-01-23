#!/bin/bash

# Clean tempdir
rm -rf tempdir
mkdir -p tempdir/templates
mkdir -p tempdir/static

# Kopieer app + html + css
cp app.py tempdir/
cp templates/index.html tempdir/templates/
cp static/style.css tempdir/static/

# Maak Dockerfile via echo
echo "FROM python:3.10-slim" > tempdir/Dockerfile
echo "RUN pip install --no-cache-dir --progress-bar off flask" >> tempdir/Dockerfile
echo "WORKDIR /app" >> tempdir/Dockerfile
echo "COPY . /app" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 app.py" >> tempdir/Dockerfile

# Build image
cd tempdir
docker build -t di3-webapp .

# Stop + remove oude container
docker stop di3-container 2>/dev/null
docker rm di3-container 2>/dev/null

# Run container
docker run -d -p 8083:8080 --name di3-container di3-webapp

# Toon containers
docker ps
