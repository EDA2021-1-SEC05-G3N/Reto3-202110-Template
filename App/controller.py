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
import datetime
import tracemalloc
import time

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la función de inicialización  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadEventos(catalog)
    loadTracks(catalog)
    loadHashtags(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory

def loadEventos(catalog):
    """
    Carga los eventos del archivo. Por cada evento se toma los datos necesarios:
    instrumentalness,  danceability, tempo, energy, id del artista, id de la pista, 
    y fecha de publicación.
    """
    videosfile = cf.data_dir + 'context_content_features-small.csv'
    
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for evento in input_file:
        cada_evento = {"instrumentalness": float(evento["instrumentalness"]),
                  "danceability": float(evento["danceability"]),
                  "tempo": float(evento["tempo"]),
                  "energy": float(evento["energy"]),
                  "artist_id": evento["artist_id"],
                  "track_id": evento["track_id"],
                  "time": datetime.datetime.strptime(evento["created_at"], '%Y-%m-%d %H:%M:%S').time(),
                  "user_id": evento["user_id"],
                  "id": evento["id"]
                  }       
        model.addEvento(catalog, cada_evento)

def loadTracks(catalog):
    """
    Carga la canción de cada evento del archivo. Por cada canción se toma el único
    dato necesario: el hashtag.
    """    
    videosfile = cf.data_dir + 'user_track_hashtag_timestamp-small.csv'
    
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for evento in input_file:
        cada_evento = {"track_id": evento["track_id"], 
                    "hashtag": evento["hashtag"].lower()
                    }
        model.addTrack(catalog, cada_evento)

def loadHashtags(catalog):
    """
    Carga los hashtags del archivo. Por cada hashtag se toma el único dato necesario:
    el vader promedio.
    """
    videosfile = cf.data_dir + 'sentiment_values.csv'
    
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for hashtag in input_file:
        try:
            cada_hashtag = {"hashtag": hashtag["hashtag"].lower(), 
                        "vader_avg": float(hashtag["vader_avg"])
                        }
            model.addHashtag(catalog, cada_hashtag)
        except:
            pass


# Funciones de consulta sobre el catálogo

def sizeList(catalog, lista):
    return model.sizeList(catalog, lista)

def sizeMap(catalog, mapa):
    return model.sizeMap(catalog, mapa)

def indexHeight(catalog):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(catalog)


def indexSize(catalog):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(catalog)


def minKey(catalog):
    """
    La menor llave del arbol
    """
    return model.minKey(catalog)


def maxKey(catalog):
    """
    La mayor llave del arbol
    """
    return model.maxKey(catalog)

def requerimiento1(catalog, menor, mayor, caracteristica):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    resp = model.requerimiento1(catalog, menor, mayor, caracteristica)
   
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory, resp

def requerimiento2(catalog, menor1, mayor1, menor2, mayor2):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    resp=model.requerimiento2(catalog, menor1, mayor1, menor2, mayor2)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory, resp

def requerimiento3(catalog, menor1, mayor1, menor2, mayor2):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    resp= model.requerimiento3(catalog, menor1, mayor1, menor2, mayor2)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory, resp
  

def requerimiento4(catalog, mapa_generos):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    resp= model.requerimiento4(catalog, mapa_generos)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory, resp

def requerimiento5(catalog, horamin, horamax):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    parte1 = model.requerimiento5_parte1(catalog, horamin, horamax)
    parte2 = model.requerimiento5_parte2(catalog, parte1[2])

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory, (parte1 , parte2)


# ======================================
# Funciones para medir tiempo y memoria
# ======================================


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
