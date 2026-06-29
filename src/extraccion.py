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
URL_BASE = "https://api.rawg.io/api/games"
JUEGOS_OBJETIVO = 60000     # ahora vamos a por la descarga grande
JUEGOS_POR_PAGINA = 40      # máximo que permite RAWG por página
ORDEN = "-added"            # ordenamos por popularidad (juegos con datos reales primero)


# ============================================================
# BLOQUE 3: Función que extrae los juegos página por página
# ============================================================
def extraer_juegos(objetivo):
    juegos_recopilados = []   # aquí iremos guardando cada juego
    pagina = 1                # empezamos por la página 1

    while len(juegos_recopilados) < objetivo:
        params = {
            "key": API_KEY,
            "page": pagina,
            "page_size": JUEGOS_POR_PAGINA,
            "ordering": ORDEN,   # orden estable para paginar miles de páginas
        }

        # Pedimos la página con hasta 3 reintentos si hay un fallo puntual de red
        respuesta = None
        for intento in range(3):
            try:
                respuesta = requests.get(URL_BASE, params=params, timeout=30)
                break
            except requests.exceptions.RequestException as e:
                print(f"Aviso: fallo de red en página {pagina}, reintento {intento+1}/3... ({e})")
                time.sleep(3)

        # Si tras 3 intentos no hubo respuesta, paramos y guardamos lo acumulado
        if respuesta is None:
            print(f"No se pudo descargar la página {pagina}. Guardamos lo que llevamos.")
            break

        # Si la API devuelve un error, paramos pero conservamos lo descargado
        if respuesta.status_code != 200:
            print(f"Error en la página {pagina}: código {respuesta.status_code}. Guardamos lo acumulado.")
            break

        datos = respuesta.json()
        resultados = datos["results"]

        # Si una página viene vacía, ya no hay más juegos
        if not resultados:
            print("No hay más juegos disponibles.")
            break

        juegos_recopilados.extend(resultados)

        # Mostramos el progreso cada 10 páginas (para no llenar la pantalla)
        if pagina % 10 == 0:
            print(f"Página {pagina} | Total acumulado: {len(juegos_recopilados)} juegos")

        pagina += 1
        time.sleep(0.5)   # pequeña pausa para no saturar la API

    return juegos_recopilados[:objetivo]


# ============================================================
# BLOQUE 4: Ejecutar la extracción y guardar en CSV
# ============================================================
if __name__ == "__main__":
    print("Iniciando extracción de juegos desde RAWG...\n")

    juegos = extraer_juegos(JUEGOS_OBJETIVO)

    # Convertimos la lista de juegos en una tabla de Pandas (DataFrame)
    df = pd.DataFrame(juegos)

    # Guardamos la tabla en un CSV dentro de data/raw (¡ojo: nuevo nombre!)
    ruta_salida = "data/raw/juegos.csv"
    df.to_csv(ruta_salida, index=False, encoding="utf-8")

    print(f"\n¡Listo! Se guardaron {len(df)} juegos en '{ruta_salida}'")
    print(f"Número de columnas obtenidas: {df.shape[1]}")
    