# ============================================================
# BLOQUE 1: Importar las herramientas que vamos a usar
# ============================================================
import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

# Cargamos la API key desde el archivo .env
load_dotenv()
API_KEY = os.getenv("RAWG_API_KEY")


# ============================================================
# BLOQUE 2: Configuración de la extracción
# ============================================================
URL_BASE = "https://api.rawg.io/api/games"  # endpoint de juegos
JUEGOS_OBJETIVO = 500    # cuántos juegos queremos en esta prueba
JUEGOS_POR_PAGINA = 40   # máximo que permite RAWG por página


# ============================================================
# BLOQUE 3: Función que extrae los juegos página por página
# ============================================================
def extraer_juegos(objetivo):
    juegos_recopilados = []   # aquí iremos guardando cada juego
    pagina = 1                # empezamos por la página 1

    # Seguimos pidiendo páginas hasta llegar al objetivo
    while len(juegos_recopilados) < objetivo:
        # Preparamos los parámetros de la petición
        params = {
            "key": API_KEY,
            "page": pagina,
            "page_size": JUEGOS_POR_PAGINA,
        }

        # Hacemos la petición a la API
        respuesta = requests.get(URL_BASE, params=params)

        # Si algo sale mal, avisamos y paramos
        if respuesta.status_code != 200:
            print(f"Error en la página {pagina}: código {respuesta.status_code}")
            break

        datos = respuesta.json()
        resultados = datos["results"]  # la lista de juegos de esta página

        # Si una página viene vacía, ya no hay más juegos
        if not resultados:
            print("No hay más juegos disponibles.")
            break

        # Añadimos los juegos de esta página a nuestra lista
        juegos_recopilados.extend(resultados)
        print(f"Página {pagina} descargada. Total acumulado: {len(juegos_recopilados)} juegos")

        pagina += 1          # pasamos a la siguiente página
        time.sleep(0.5)      # pequeña pausa para no saturar la API

    # Devolvemos solo la cantidad objetivo (por si nos pasamos un poco)
    return juegos_recopilados[:objetivo]


# ============================================================
# BLOQUE 4: Ejecutar la extracción y guardar en CSV
# ============================================================
if __name__ == "__main__":
    print("Iniciando extracción de juegos desde RAWG...\n")

    juegos = extraer_juegos(JUEGOS_OBJETIVO)

    # Convertimos la lista de juegos en una tabla de Pandas (DataFrame)
    df = pd.DataFrame(juegos)

    # Guardamos la tabla en un archivo CSV dentro de data/raw
    ruta_salida = "data/raw/juegos_muestra.csv"
    df.to_csv(ruta_salida, index=False, encoding="utf-8")

    print(f"\n¡Listo! Se guardaron {len(df)} juegos en '{ruta_salida}'")
    print(f"Número de columnas obtenidas: {df.shape[1]}")