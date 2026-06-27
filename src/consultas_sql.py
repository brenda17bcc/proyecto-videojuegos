# ============================================================
# BLOQUE 1: Conexión a la base de datos
# ============================================================
import sqlite3
import pandas as pd

RUTA_DB = "data/videojuegos.db"
conexion = sqlite3.connect(RUTA_DB)


# Función auxiliar: ejecuta una consulta SQL y la muestra bonita
def consultar(titulo, sql):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)
    resultado = pd.read_sql_query(sql, conexion)
    print(resultado.to_string(index=False))


# ============================================================
# BLOQUE 2: CONSULTA 1 - SELECT simple
# ¿Cuántos juegos hay en total en la base de datos?
# ============================================================
consultar(
    "CONSULTA 1: Total de juegos almacenados",
    "SELECT COUNT(*) AS total_juegos FROM juegos;"
)


# ============================================================
# BLOQUE 3: CONSULTA 2 - SELECT con ORDER BY y LIMIT
# Los 10 juegos mejor valorados (con al menos algo de votos)
# ============================================================
consultar(
    "CONSULTA 2: Top 10 juegos con mejor rating",
    """
    SELECT name, rating, metacritic, released
    FROM juegos
    WHERE rating > 0
    ORDER BY rating DESC
    LIMIT 10;
    """
)


# ============================================================
# BLOQUE 4: CONSULTA 3 - JOIN entre las dos tablas
# Rating promedio por género (¡aquí brilla el diseño relacional!)
# ============================================================
consultar(
    "CONSULTA 3: Rating promedio por género (JOIN)",
    """
    SELECT g.genero,
           COUNT(*) AS cantidad_juegos,
           ROUND(AVG(j.rating), 2) AS rating_promedio
    FROM juegos j
    JOIN generos g ON j.id = g.id_juego
    WHERE j.rating > 0
    GROUP BY g.genero
    ORDER BY rating_promedio DESC
    LIMIT 15;
    """
)


# ============================================================
# BLOQUE 5: CONSULTA 4 - Agregación con GROUP BY
# ¿Cuántos juegos se lanzaron por año? (los más recientes)
# ============================================================
consultar(
    "CONSULTA 4: Juegos lanzados por año (últimos años)",
    """
    SELECT SUBSTR(released, 1, 4) AS anio,
           COUNT(*) AS cantidad
    FROM juegos
    WHERE released IS NOT NULL
    GROUP BY anio
    ORDER BY anio DESC
    LIMIT 10;
    """
)


# ============================================================
# BLOQUE 6: Cerrar la conexión
# ============================================================
conexion.close()
print("\n" + "=" * 60)
print("Consultas finalizadas. Conexión cerrada.")
print("=" * 60)