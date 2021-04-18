"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newAnalyzer()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):

    loadEventos(catalog)


def loadEventos(catalog):
    """
    Carga los libros del archivo.  Por cada video se toman los datos necesarios:
    video id, trending date, category id, views, nombre del canal, país, nombre del 
    video, likes, dislikes, fecha de publicación, likes y tags.
    """
    
    videosfile = cf.data_dir + 'context_content_features-small.csv '
    
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for evento in input_file:
        cada_evento = {"instrumentalness": float(evento["instrumentalness"]),
                  "liveness": float(evento["liveness"]),
                  "speechiness": float(evento["speechiness"]),
                  "danceability": float(evento["danceability"]),
                  "valence": float(evento["valence"]),
                  "loudness": float(evento["loudness"]),
                  "tempo": float(evento["tempo"]),
                  "acousticness": float(evento["acousticness"]),
                  "energy": float(evento["energy"]),
                  "mode": float(evento["mode"]),
                  "key": float(evento["key"]),
                  "artist_id": evento["artist_id"],
                  "track_id": evento["track_id"]}
                  
        model.addEvento(catalog, cada_evento)

def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)


def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)

def requerimiento1(catalog, menor, mayor, caracteristica):
    return model.requerimiento1(catalog, menor, mayor, caracteristica)

def requerimiento2(catalog, menor1, mayor1, menor2, mayor2):
    return model.requerimiento2(catalog, menor1, mayor1, menor2, mayor2)

def requerimiento3(catalog, menor1, mayor1, menor2, mayor2):
    return model.requerimiento3(catalog, menor1, mayor1, menor2, mayor2)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
