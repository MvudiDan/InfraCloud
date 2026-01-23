#!/bin/bash

# Maak tijdelijke map
mkdir tempdir

# Kopieer app
cp app.py tempdir/.

# Maak Dockerfile via echo
echo "FROM python:3.10-slim" > tempdir/Dockerfile
echo "RUN pip install --no-cache-dir --progress-bar off flask" >> tempdir/Dockerfile
echo "WORKDIR /app" >> tempdir/Dockerfile
echo "COPY app.py /app/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /app/app.py" >> tempdir/Dockerfile

# Build image
cd tempdir
docker build -t di2-webapp .

# Run container
docker run -t -d -p 8082:8080 --name di2-container di2-webapp

# Toon containers
docker ps
