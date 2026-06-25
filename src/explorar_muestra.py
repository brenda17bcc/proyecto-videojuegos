import pandas as pd

# Cargamos el CSV de muestra que acabamos de generar
df = pd.read_csv("data/raw/juegos_muestra.csv")

# Información general: cuántas filas y columnas
print("Forma del dataset (filas, columnas):", df.shape)

# Lista de todas las columnas disponibles
print("\nColumnas disponibles:")
for columna in df.columns:
    print("  -", columna)

# Vistazo a las primeras filas de algunas columnas clave
print("\nPrimeras filas (columnas seleccionadas):")
columnas_clave = ["name", "released", "rating", "metacritic", "playtime"]
print(df[columnas_clave].head(10))