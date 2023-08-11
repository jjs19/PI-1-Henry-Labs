![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

# PI-1-Henry-Data-PT02
## Proyecto individual 1
## Scarpeccio Julián Jesús

## Bienvenidos a mi repositorio de GitHub del Proyecto Individual número 1 de la carrera Data Science Part Time 02 de Henry.

En el presente proyecto se trabajó con datasets brindados por la academia, en este caso dos datasets de Peliculas, los cuales no estan en el Repo por una cuestión de ahorro de espacio. 
Los mismos los pueden encontrar en los siguientes links:

**-movies_dataset:**  https://drive.google.com/file/d/11PW-n4obMTgK-YZ9VD3cVJwiabr7hY1c/view?usp=share_link

**-credits:** https://drive.google.com/file/d/1HxSWoxncj9Waqn2k5BJdeRaHLuZ4-MoE/view?usp=share_link


## Descripción de archivos y pasos realizados.

### 1ro: Levantamos los datasets y realizamos el proceso de ETL.
ETL es el acrónimo de "Extract, Transform, Load" (Extraer, Transformar, Cargar, en español), y se refiere a un proceso utilizado en la gestión y análisis de datos en el ámbito de la tecnología de la información y la informática.

**Extract (Extraer):** En esta etapa, los datos se obtienen de diversas fuentes, en este caso en particular fue brindada por la academia. La extracción implica recopilar los datos necesarios para su posterior análisis y procesamiento.
**Transform (Transformar):** Una vez que los datos se han extraído, generalmente necesitan ser limpiados, enriquecidos y transformados en un formato adecuado para su análisis. En esta etapa, se aplican diversas operaciones de limpieza, filtrado, agregación y manipulación de datos para garantizar que sean coherentes y útiles para el análisis.
**Load (Cargar):** Una vez que los datos han sido extraídos y transformados, se cargan en un destino final. El objetivo es que los datos procesados y transformados estén disponibles para su consulta y análisis por parte de los usuarios o sistemas que los necesiten.

** El Proceso de ETL lo pueden encontrar en el archivo: PI_1_JJS_ETL_EDA Movies.ipynb , aquí se encontrara con el codigo realizado y comentado paso a paso lo que se fue haciendo para su claro entendimiento **

## 2do: Realizamos el Análisis Exploratorio de Datos (EDA)
**EDA** son las siglas de "Exploratory Data Analysis" en inglés, lo que se traduce al español como "Análisis Exploratorio de Datos". 
EDA es una fase crucial en el proceso de análisis de datos, donde se lleva a cabo una exploración inicial y visualización de los datos antes de aplicar métodos más avanzados de modelado o análisis estadístico.

El objetivo principal del EDA es comprender la estructura y las características de los datos, detectar patrones, tendencias, valores atípicos y relaciones entre variables. Durante esta fase, los analistas pueden utilizar gráficos, tablas, estadísticas descriptivas y técnicas visuales para obtener una visión general de los datos y generar hipótesis iniciales.

** Este proceso se puede encontrar en el siguiente archivo: PI_1_JJS_ETL_EDA Movies.ipynb con los respectivos comentarios de código y las conclusiones de cada paso que se fue haciendo. **

## 3ro: Se realizaron las consultas solicitadas dentro de los objetivos del Proyecto para su posterior procesamiento en una API
Las consultas requeridas eran las siguientes:

*Deben crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).

def peliculas_idioma( Idioma: str ): Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). Debe devolver la cantidad de películas producidas en ese idioma.
                    Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma

def peliculas_duracion( Pelicula: str ): Se ingresa una pelicula. Debe devolver la duracion y el año.
                    Ejemplo de retorno: X . Duración: x. Año: xx

def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
                    Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia total de x y una ganancia promedio de xx

def peliculas_pais( Pais: str ): Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
                    Ejemplo de retorno: Se produjeron X películas en el país X

def productoras_exitosas( Productora: str ): Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.
                    Ejemplo de retorno: La productora X ha tenido un revenue de x

def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.*

**El proceso de armado de consultas se encuentra en el siguiente archivo: PI_1_JJS_Consultas_DFfinal.ipynb con las respectivas explicaciones de codigo en el mismo. **
Por otro lado el archivo main.py es el que se creo con las consultas adaptadas a FastApi. 

Una API (Interfaz de programación de aplicaciones) es un conjunto de requisiciones que permite la comunicación de datos entre aplicaciones. En nuestro caso conectamos las consultas creadas en Python con FastApi para procesar las consultas solicitadas de una manera simple y de facil acceso.

## 4to: Por último se realizó un modelo de Machine Learning de recomendacion de Peliculas
El trabajo realizado para esta sección se encuentra en la carpeta: PI_1_JJS_ML Movies.ipynb, donde se explica el paso a paso realizado y la teoría del modelo que se eligió.
Tambien se adaptó la formula al formato FastApi en el archivo: main.py para que corra en la API correcatmente.

## Resumen Archivos:

**main.py:** API y Consultas
**PI_1_JJS_ETL_EDA Movies.ipynb** Carga de Datasets, ETL y EDA
**PI_1_JJS_Consultas_DFfinal.ipynb** Prueba Consultas API
**PI_1_JJS_ML Movies.ipynb** Prueba del modelo de Machine Learning

**mi_df_consultas** Creé un dataset reducio para poder correr las consultas en Render, ya que la version gratuita no soportaba un dataset muy grande
**mi_df_ml** Se aplicó lo mismo para el modelo de recomendación.

## Link a Render Consultas: https://proyecto-ind-1-henry.onrender.com/docs#/
## Link al video demostración: https://drive.google.com/file/d/1e_DYa52se2kS8yqHfvlq2i70DadH8lPY/view?usp=share_link 

**De esta manera finalizo mi Proyecto Individual 1.**

**Muchas Gracias** 

**Julián Jesús Scarpeccio**





