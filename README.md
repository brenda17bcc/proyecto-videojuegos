# 🎮 ¿Qué hace que un videojuego triunfe?

Proyecto final de Machine Learning — Predicción del rating de videojuegos a partir de datos reales de la API pública de RAWG.

## 📌 Descripción del problema

A partir de las características de un videojuego (género, plataformas, desarrolladora, clasificación ESRB, tiempo de juego, fecha de lanzamiento, etc.), se construye un modelo de **regresión** capaz de predecir su **rating** (de 0 a 5).

Como extensión, se plantea también una versión de **clasificación** ("¿será un éxito? rating ≥ 4: sí/no") para obtener una conclusión más directa.

## 🗂️ Fuente de datos

- **API:** RAWG Video Games Database (https://rawg.io/apidocs)
- **Volumen:** más de 899.000 videojuegos disponibles
- **Acceso:** API pública gratuita mediante clave de autenticación

## ✅ Cumplimiento de requisitos
lmacenamiento en base de datos | ✔️ SQLite (Paso 3) |
| Despliegue web | ✔️ Streamlit (Paso 7) |

## 🛠️ Tecnologías

Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn · SQLAlchemy / SQLite · Streamlit

## 📁 Estructura del proyecto
## 📅 Plan de trabajo

1. Definición del problema y montaje del entorno
2. Obtención y carga de datos desde la API → CSV
3. Almacenamiento en base de datos + consultas SQL
4. Análisis descriptivo
5. EDA completo y división train/test
6. Construcción y optimización del modelo
7. Despliegue de la aplicación web

## 👤 Autora 

Brenda Campos Cobeñas — Proyecto final del bootcamp de Data Science / Machine Learning
| Requisito | Estado |
|-----------|--------|
| Mínimo 60.000 filas | ✔️ Holgura amplia (catálogo de +899.000 juegos) |
| Mínimo 20 variables predictoras | ✔️ Vía extracción + feature engineering |
| Al menos 1 variable categórica | ✔️ Género, plataforma, ESRB, desarrolladora |
| Obtención por API pública (no CSV plano) | ✔️ API REST de RAWG |
| Almacenamiento en base de datos | ✔️ SQLite (Paso 3) |
| Despliegue web | ✔️ Streamlit (Paso 7) |

## 🛠️ Tecnologías

Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn · SQLAlchemy / SQLite · Streamlit

## 📁 Estructura del proyecto
## 📅 Plan de trabajo

1. Definición del problema y montaje del entorno
2. Obtención y carga de datos desde la API → CSV
3. Almacenamiento en base de datos + consultas SQL
4. Análisis descriptivo
5. EDA completo y división train/test
6. Construcción y optimización del modelo
7. Despliegue de la aplicación web

## 👤 Autora 

Brenda Campos Cobeñas — Proyecto final del bootcamp de Data Science / Machine Learning