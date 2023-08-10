#main.py

from fastapi import FastAPI
import pandas as pd
import numpy as np

# Crear una instancia de la aplicación FastAPI
app = FastAPI(docs_url="/docs")

final = pd.read_csv('mi_df_consultas')
df_final = pd.DataFrame(final)

# Definir una ruta y una función de manejo para esa ruta
@app.get("/")
def read_root():
    return {"Hello": "World"}

def peliculas_idioma(idioma):
    cantidad = df_final['spoken_languages'].apply(lambda x: idioma in x).sum()
    mensaje = f"Se han lanzado '{cantidad}' de peliculas en ese Idioma"
    return mensaje

# Route to call the function with a query parameter 'idioma'
@app.get("/peliculas/")
def get_peliculas_idioma(idioma: str):
    resultado = peliculas_idioma(idioma)
    return {"mensaje": resultado}

def peliculas_duracion(nombre_pelicula):
    """
    Esta función toma el nombre de una película y devuelve la duración y el año de lanzamiento
    de la película solicitada.
    """
    pelicula = df_final[df_final['title'] == nombre_pelicula]

    if pelicula.empty:
        return "Película no encontrada en la base de datos."

    duracion = pelicula['runtime'].values[0]
    ano_lanzamiento = pelicula['release_year'].values[0]

    mensaje = f"La película '{nombre_pelicula}' tiene una duración de {duracion} minutos y fue lanzada en el año {ano_lanzamiento}."

    return mensaje

# Definir una ruta en FastAPI
@app.get("/peliculas/{nombre_pelicula}")
def get_pelicula(nombre_pelicula: str):
    resultado = peliculas_duracion(nombre_pelicula)
    return {"resultado": resultado}

# Definir la función
def franquicia(Franquicia: str):
    """
    Esta función toma el nombre de una franquicia y devuelve información sobre la misma,
    incluyendo el total de películas, ganancia total y promedio de ganancia.
    """
    franquicia_df = df_final[df_final['belongs_to_collection'] == Franquicia]

    if franquicia_df.empty:
        return "Franquicia no encontrada en la base de datos."

    total_peliculas = franquicia_df.shape[0]
    total_return = franquicia_df['return'].sum()
    promedio_return = franquicia_df['return'].mean()

    mensaje = f"La franquicia '{Franquicia}' cuenta con un total de {total_peliculas} películas con las cuales obtuvo una Ganancia Total de ${total_return} y en promedio ${promedio_return}."

    return mensaje

# Definir una ruta en FastAPI
@app.get("/franquicias/{Franquicia}")
def get_franquicia(Franquicia: str):
    resultado = franquicia(Franquicia)
    return {"resultado": resultado}


# Definir la función
def peliculas_pais(pais):
    """
    Esta función toma el nombre de un país y devuelve la cantidad de películas lanzadas en ese país.
    """
    cantidad = df_final['production_countries'].apply(lambda x: pais in x).sum()
    mensaje = f"Se han lanzado '{cantidad}' películas en '{pais}'."
    return mensaje

# Definir una ruta en FastAPI
@app.get("/peliculas_pais/{pais}")
def get_peliculas_pais(pais: str):
    resultado = peliculas_pais(pais)
    return {"resultado": resultado}

# Definir la función
def productoras_exitosas(productora):
    """
    Esta función toma el nombre de una productora y devuelve información sobre la misma,
    incluyendo el total de películas producidas y el revenue total.
    """
    productora_df = df_final[df_final['production_companies'].str.contains(productora)]

    if productora_df.empty:
        return f"No se encontraron resultados para la productora '{productora}'."

    total_peliculas = productora_df.shape[0]
    total_revenue = productora_df['revenue'].sum()

    mensaje = f"La productora '{productora}' ha tenido un revenue de ${total_revenue} y ha producido un total de {total_peliculas} películas."

    return mensaje

# Definir una ruta en FastAPI
@app.get("/productoras/{productora}")
def get_productora(productora: str):
    resultado = productoras_exitosas(productora)
    return {"resultado": resultado}

# Definir la función
def get_director_info(director):
    """
    Esta función toma el nombre de un director y devuelve información sobre las películas dirigidas por él,
    incluyendo el revenue total y detalles de las películas.
    """
    relevant_columns = ['director', 'title', 'release_year', 'budget', 'return']
    df_cleaned = df_final.dropna(subset=relevant_columns)

    director_df = df_cleaned[df_cleaned['director'].str.contains(director, case=False)]

    if director_df.empty:
        return f"No se encontraron resultados para el director '{director}'."

    total_revenue = director_df['return'].sum()

    movie_info = []
    for index, row in director_df.iterrows():
        movie_name = row['title']
        release_year = row['release_year']
        budget = row['budget']
        revenue = row['return']

        movie_info.append({"movie_name": movie_name, "release_year": release_year, "budget": budget, "revenue": revenue})

    mensaje = f"El director '{director}' ha tenido un revenue total de ${total_revenue} y ha producido las siguientes películas:"
    return mensaje, movie_info

# Definir una ruta en FastAPI
@app.get("/directores/{director}")
def get_director(director: str):
    resultado, info_peliculas = get_director_info(director)
    return {"resultado": resultado, "info_peliculas": info_peliculas}

