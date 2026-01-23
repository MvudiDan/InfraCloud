created by: Mvudi Dan Landu Muana
creation date: nov 2025
Last Update: -

keywords:
- CI/CD
- Jenkins
- GitHub
- Docker
- Pipeline
- Continuous Integration
- Continuous Deployment
- Automation
- Build and test
- Flask application
- Bash scripting
- DevOps
- Version control


---
Notes:sample_app.py (fase 1)
Basis Flask webapp die een HTTP-response teruggeeft en lokaal kan draaien.

sample-app.sh (fase 2)
Bash script dat automatisch:

een Dockerfile genereert

een Docker image bouwt

en de container start

sample_app.py & sample-app.sh (fase 3)
Poortwijziging van 8080 naar 5050 om conflicten met Jenkins te vermijden.

GitHub repository
Toevoegen van version control door commits en pushes van codewijzigingen.

Jenkins Docker container
Installatie en configuratie van Jenkins in Docker inclusief volume mounts en Docker-inside-Docker setup.

Jenkins Job: BuildAppJob
Automatisch:

code ophalen uit GitHub

build uitvoeren via sample-app.sh

Jenkins Job: TestAppJob
Automatische test met curl om te verifiëren dat de webapp correct draait.

Jenkins Pipeline: SamplePipeline
Geautomatiseerde CI/CD pipeline met stages:

Preparation

Build

Results