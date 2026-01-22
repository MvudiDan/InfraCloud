created by: Mvudi Dan Landu Muana
creation date: nov 2025
Last Update: -

keywords:
- Graphhopper API
- REST API
- Python
- JSON parsing
- Geocoding API
- Routing API
- HTTP GET
- API key authentication
- User input handling
- Error handling
- Distance & time calculation
- Command-line application


---
Notes:Dit project is opgebouwd in meerdere Python-bestanden, waarbij elke nieuwe file extra functionaliteit toevoegt:

  - graphhopper_parse-json_1.py
    Basis API-call naar de Graphhopper Geocoding API en weergeven van ruwe JSON-data.

  - graphhopper_parse-json_2.py
    Toevoegen van een geocoding() functie om latitude en longitude op te halen voor meerdere locaties.

  - graphhopper_parse-json_3.py
    Gebruikersinput toegevoegd voor start- en eindlocatie met een herhaalbare loop.

  - graphhopper_parse-json_4.py
    Foutafhandeling toegevoegd voor lege input, ongeldige locaties en foutieve API keys.

  - graphhopper_parse-json_5.py
    Integratie van de Routing API om afstand en reistijd te berekenen tussen twee locaties.

  - graphhopper_parse-json_6.py
    Parsing van route-instructies en weergeven van stap-voor-stap navigatie.

  - graphhopper_parse-json_7.py
    Ondersteuning voor meerdere vervoersmodi (car, bike, foot) en volledige applicatieflow.