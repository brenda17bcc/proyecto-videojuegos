# ============================================================
# BLOQUE 1: Importar herramientas
# ============================================================
import ast
import sqlite3
import pandas as pd

RUTA_CSV = "data/raw/juegos.csv"
RUTA_DB = "data/videojuegos.db"   # aquí vivirá nuestra base de datos


# ============================================================
# BLOQUE 2: Cargar el CSV y seleccionar columnas útiles
# ============================================================
print("Cargando el CSV...")
df = pd.read_csv(RUTA_CSV)

# Nos quedamos con las columnas que aportan al análisis (tabla principal)
columnas_juegos = [
    "id", "name", "released", "rating", "rating_top",
    "metacritic", "playtime", "ratings_count", "added", "suggestions_count",
]
df_juegos = df[columnas_juegos].copy()

print(f"Tabla 'juegos' preparada: {df_juegos.shape[0]} filas")


# ============================================================
# BLOQUE 3: Construir la tabla de géneros (diseño relacional)
# ============================================================
# La columna 'genres' viene como texto que representa una lista de diccionarios.
# Ejemplo: "[{'id': 4, 'name': 'Action'}, {'id': 5, 'name': 'RPG'}]"
# La recorremos y creamos una fila por cada (juego, género).

filas_generos = []

for _, fila in df.iterrows():
    id_juego = fila["id"]
    texto_generos = fila["genres"]

    # Si el juego no tiene géneros, lo saltamos
    if pd.isna(texto_generos):
        continue

    # Convertimos el texto en una lista de Python de verdad
    try:
        lista_generos = ast.literal_eval(texto_generos)
    except (ValueError, SyntaxError):
        continue

    # Por cada género del juego, guardamos una fila (id_juego, nombre_genero)
    for genero in lista_generos:
        filas_generos.append({
            "id_juego": id_juego,
            "genero": genero["name"],
        })

df_generos = pd.DataFrame(filas_generos)
print(f"Tabla 'generos' preparada: {df_generos.shape[0]} relaciones juego-género")


# ============================================================
# BLOQUE 4: Guardar todo en la base de datos SQLite
# ============================================================
print("\nGuardando en la base de datos SQLite...")

# Nos conectamos (si el archivo .db no existe, se crea solo)
conexion = sqlite3.connect(RUTA_DB)

# Volcamos cada DataFrame como una tabla. if_exists="replace" la regenera limpia.
df_juegos.to_sql("juegos", conexion, if_exists="replace", index=False)
df_generos.to_sql("generos", conexion, if_exists="replace", index=False)

# Cerramos la conexión (buena práctica: siempre cerrar)
conexion.close()

print(f"¡Listo! Base de datos creada en '{RUTA_DB}'")
print("Tablas creadas: 'juegos' y 'generos'")