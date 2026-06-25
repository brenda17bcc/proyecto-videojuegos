import os
import requests
from dotenv import load_dotenv

# Cargamos la API key desde el archivo .env 
load_dotenv()
API_KEY = os.getenv("RAWG_API_KEY")

# Petición pequeña: pedimos 5 juegos para comprobar que la conexión funciona
url = "https://api.rawg.io/api/games"
params = {"key": API_KEY, "page_size": 5}

respuesta = requests.get(url, params=params)

# Verificamos que la API respondió bien (código 200 = OK)
print("Código de estado:", respuesta.status_code)

if respuesta.status_code == 200:
    datos = respuesta.json()
    print("Total de juegos en la base de datos:", datos["count"])
    print("\nPrimeros 5 juegos recibidos:")
    for juego in datos["results"]:
        print(f"  - {juego['name']} | rating: {juego['rating']} | lanzamiento: {juego['released']}")
else:
    print("Algo falló. Revisa tu API key en el archivo .env")