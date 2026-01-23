created by: Mvudi Dan Landu Muana
creation date: nov 2025
Last Update: -

keywords:
- Docker
- Flask
- Python
- Web application
- Dockerfile
- Bash scripting
- REST basics

---
Notes:Dit project is stapsgewijs opgebouwd waarbij elke file extra functionaliteit toevoegt voor het bouwen en deployen van een webapplicatie in een Docker-container:

user-input.sh
Basis bash script voor gebruikersinput en het oefenen met uitvoerbare scripts.

sample_app.py (fase 1)
Simpele Flask webapp die het IP-adres van de client toont via een HTTP-response.

sample_app.py (fase 2)
Toevoegen van HTML-rendering met index.html en style.css via render_template.

index.html
Webpagina met dynamische content die het client IP-adres toont.

style.css
Basis styling voor de webpagina.

sample-app.sh
Bash script dat automatisch:

directories aanmaakt

websitebestanden kopieert

een Dockerfile genereert

de Docker image bouwt

en de container start

Dockerfile (gegenereerd)
Definieert de Docker image met Python, Flask, webbestanden en exposed poort.