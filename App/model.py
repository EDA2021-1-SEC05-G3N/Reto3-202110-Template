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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf
import random

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """ Inicializa el catálogo

    Crea un diccionario cuyos valores serán las estructuras de datos.
    Se crea un Ordered Map para cada característica de contenido utilizada.
    Además, se crea un Map para las pistas y otro Map los hashtags.

    Retorna el catálogo inicializado.
    """
    catalog = {'instrumentalness': None,
                "danceability": None,
                "tempo": None,
                "energy": None,

                "eventos": None, # Lista con todos los eventos de context_content
                "artistas": None, # Mapa con artistas no repetidos

                "time": None,

                "track_id": None, # Mapa de pistas cuyo valor es un mapa con sus hashtags únicos
                "hashtag": None # Mapa de hashtags cuyo valor es su vader_avg
                }

    catalog['instrumentalness'] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["danceability"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["tempo"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["energy"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)

    catalog["eventos"] = lt.newList("ARRAY_LIST")
    catalog["artist_id"] = mp.newMap(maptype="PROBING", loadfactor = 0.5)

    catalog["time"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)

    catalog["track_id"] = mp.newMap(maptype="PROBING", loadfactor = 0.5)
    catalog["hashtag"] = mp.newMap(maptype="PROBING", loadfactor = 0.5)

    return catalog

# Funciones para agregar información al catálogo

def addEvento(catalog, evento):

    addEventoCaracteristica(catalog, evento, 'instrumentalness')
    addEventoCaracteristica(catalog, evento, 'danceability')
    addEventoCaracteristica(catalog, evento, 'tempo')
    addEventoCaracteristica(catalog, evento, 'energy')
    addEventoCaracteristica(catalog, evento, 'time')
    addArtista(catalog, evento)
    lt.addLast(catalog["eventos"], evento)


def addArtista(catalog, evento):

    artista_map = catalog['artist_id']
 
    artista = evento['artist_id']

    existartista = mp.contains(artista_map, artista)

    if not existartista:
        artistas = newArtista(evento)
        mp.put(artista_map, artista, artistas)

def newArtista(evento):
    
    entry = {'artista': "", "vader_avg": None}
    entry['artista'] = evento["artist_id"]
    entry['vader_avg'] = evento["artist_id"]
    return entry


def addEventoCaracteristica(catalog, evento, CARACTERISTICA):
    """
    Esta funcion adiciona un evento al Map de la característica dada 
    (e.g. instrumentalness). Los eventos se guardan en un Map, donde 
    la llave es el valor de instrumentalness y el valor es la lista
    de eventos con ese instrumentalness.
    """

    caracter_map = catalog[CARACTERISTICA]
 
    ValorCaracter = evento[CARACTERISTICA]

    existValorCaracteristica = om.contains(caracter_map, ValorCaracter)

    if existValorCaracteristica:
        entry = om.get(caracter_map, ValorCaracter)
        caracter_values = me.getValue(entry)
    else:
        caracter_values = newValorCaracteristica(ValorCaracter, CARACTERISTICA)
        om.put(caracter_map, ValorCaracter, caracter_values)
    lt.addLast(caracter_values, evento)
 
def newValorCaracteristica(ValorCaracteristica, CARACTERISTICA):
    entry = lt.newList('ARRAY_LIST')
    return entry


def addTrack(catalog, evento):

    track_map = catalog['track_id']
 
    track_id = evento['track_id']

    existtrack = mp.contains(track_map, track_id)

    if existtrack:
        hashtags = me.getValue(mp.get(track_map, track_id))
    else:
        hashtags = newTrack(track_id)
        mp.put(track_map, track_id, hashtags)

    mp.put(hashtags, evento["hashtag"], None) 

def newTrack(track_id):
    entry = mp.newMap(maptype="PROBING", loadfactor = 0.5)
    return entry


def addHashtag(catalog, evento):

    hashtag_map = catalog['hashtag']
 
    hashtag = evento['hashtag']

    existhashtag = mp.contains(hashtag_map, hashtag)

    if not existhashtag:
        vader = newHashtag(evento)
        mp.put(hashtag_map, hashtag, vader)

def newHashtag(evento):
    entry = evento["vader_avg"]
    return entry


# Funciones de consulta

def sizeList(catalog, lista):
    """
    Número de elementos en la lista del catálogo
    """
    return lt.size(catalog[lista])

def sizeMap(catalog, mapa):
    """
    Número de elementos en el mapa del catálogo
    """
    return mp.size(catalog[mapa])


# Funciones de requerimientos

def requerimiento1(catalog, menor, mayor, caracteristica):
    """
    Devuelve las reproducciones (y artistas únicos) dado un rango de característica
    """
    mapa_final = om.newMap("RBT")
    # Mapa donde se guardan los artistas sin repeticiones que cumplen con el rango

    lista_rango = om.values(catalog[caracteristica], menor, mayor)
    # Lista de listas de eventos que cumplen con el rango de la característica

    # Se recorre la lista de listas, contando el total de eventos y añadiendo los
    # artistas al mapa como llaves, cuyo valor se eligió al azar
    eventos = 0
    for lista_caract in lt.iterator(lista_rango):
        eventos += lt.size(lista_caract)
        for e in lt.iterator(lista_caract):
            om.put(mapa_final, e['artist_id'], "Maria José")

    tamaño_mapa = om.size(mapa_final)

    return eventos, tamaño_mapa, mapa_final


def requerimiento2(catalog, menor1, mayor1, menor2, mayor2):
    """
    Devuelve el total de canciones únicas y un mapa con 5 canciones
    aleatorias que cumplen con dos rangos de características 
    """
    # Mapa donde se guardan las canciones que cumplen con el rango 
    # de danceability, el valor es una tupla con el energy y el 
    # danceability de la canción
    mapa_dance = om.newMap('BST')

    # Lista de listas de eventos que cumplen con el rango de danceability
    lista_rango = om.values(catalog['danceability'], menor2, mayor2)

    for lista_energy in lt.iterator(lista_rango):
        for e in lt.iterator(lista_energy):
            om.put(mapa_dance, e['track_id'], (e['energy'], e['danceability']))

    # Lista de las canciones que cumplen con el danceability 
    canciones = om.keySet(mapa_dance)

    # Se recorre la lista de canciones que cumple con danceability y
    # se revisa cuáles de esas no cumplen con el rango de energy y 
    # se eliminan del mapa 
    for cancion in lt.iterator(canciones):
        energy = (me.getValue(om.get(mapa_dance, cancion)))[0]
        dance = (me.getValue(om.get(mapa_dance, cancion)))[1]
        if not (energy <= mayor1 and energy >= menor1):
            om.remove(mapa_dance, cancion)
   
    # Se obtiene el tamaño del mapa
    tamaño = om.size(mapa_dance) 

    # Se crea un mapa para guardar las llaves aleatorias y sus valores
    mapa_aleatorias = om.newMap('RBT')

    # Se obtiene una lista con cinco números aleatorios no repetidos 
    # que estén dentro del rango del tamaño 
    lista_cinco_aleatorios = random.sample(range(tamaño), 5)

    for i in lista_cinco_aleatorios:
        llave_aleatoria = om.select(mapa_dance, i)
        valor = me.getValue(om.get(mapa_dance, llave_aleatoria))
        om.put(mapa_aleatorias, llave_aleatoria, valor)

    return tamaño, mapa_aleatorias


def requerimiento3(catalog, menor1, mayor1, menor2, mayor2):
    """
    Devuelve el total de canciones únicas y un mapa con 5 canciones
    aleatorias que cumplen con dos rangos de características 
    """
    # Mapa donde se guardan las canciones que cumplen con el rango 
    # de tempo, el valor es una tupla con el instrumentalness y el 
    # energy de la canción
    mapa_tempo = om.newMap('BST')

    # Lista de listas de eventos que cumplen con el rango de tempo
    lista_rango = om.values(catalog['tempo'], menor2, mayor2)

    for lista_instrumentalness in lt.iterator(lista_rango):
        for e in lt.iterator(lista_instrumentalness):
            om.put(mapa_tempo, e['track_id'], (e['instrumentalness'], e['tempo']))

    # Lista de las canciones que cumplen con el tempo
    canciones = om.keySet(mapa_tempo)

    # Se recorre la lista de canciones que cumple con tempo y 
    # se revisa cuáles de esas no cumplen con el rango de 
    # instrumentalness y se eliminan del mapa 
    for cancion in lt.iterator(canciones):
        instrumental = (me.getValue(om.get(mapa_tempo, cancion)))[0]
        tempo = (me.getValue(om.get(mapa_tempo, cancion)))[1]
        if not (instrumental <= mayor1 and instrumental >= menor1):
            om.remove(mapa_tempo, cancion)

    # Se obtiene el tamaño del mapa
    tamaño = om.size(mapa_tempo) 

    # Se crea un mapa para guardar las 5 llaves aleatorias y sus valores
    mapa_aleatorias = om.newMap('RBT')

    # Se obtiene una lista con cinco números aleatorios no repetidos 
    # que estén dentro del rango del tamaño 
    lista_cinco_aleatorios = random.sample(range(tamaño), 5)

    for i in lista_cinco_aleatorios:
        llave_aleatoria = om.select(mapa_tempo, i)
        valor = me.getValue(om.get(mapa_tempo, llave_aleatoria))
        om.put(mapa_aleatorias, llave_aleatoria, valor)

    return tamaño, mapa_aleatorias


def requerimiento4(catalog, mapa_generos):
    """
    Devuelve el total de eventos dados los géneros y un mapa de géneros cuya valor
    es una tupla que contiene: el número de eventos, los artistas únicos, el mapa 
    de artistas únicos, el valor mínimo y el valor máximo
    """
    # Se hace un conteo de todas las reproducciones
    eventos_total = 0

    # Se recorre el mapa con los generos
    for genero in lt.iterator(om.keySet(mapa_generos)):
        # Se toman los límites de tempo del género  
        menor = me.getValue(om.get(mapa_generos, genero))[0]
        mayor = me.getValue(om.get(mapa_generos, genero))[1]
        # Se llama al Req. 1
        eventos, tamaño_mapa, mapa = requerimiento1(catalog, menor, mayor, 'tempo')
        # Se agrega al mismo mapa una tupla con los datos necesarios de cada género
        om.put(mapa_generos, genero, (eventos, tamaño_mapa,  mapa, menor, mayor))
        # Se suman los eventos de cada género al contador general
        eventos_total += eventos

    return mapa_generos, eventos_total


def requerimiento5_parte1(catalog, horamin, horamax):
    """
    Devuelve el total de eventos dados los géneros y un mapa de géneros cuya valor
    es una tupla que contiene: el número de eventos, los artistas únicos, el mapa 
    de artistas únicos, el valor mínimo y el valor máximo
    """
    # Lista de listas de eventos que cumplen con el rango de horas
    lista_rango =  om.values(catalog['time'], horamin, horamax)

    # Mapa con cada uno de los géneros musicales como llaves y como valor 
    # tiene una lista donde se guardan los eventos del género
    mapa_generos = mp.newMap(numelements = 11, maptype="PROBING", loadfactor = 0.5)
    # Se recorre la lista de listas, obteniendo cada evento que cumple 
    # con el rango de horas
    for lista_hora in lt.iterator(lista_rango):
        for e in lt.iterator(lista_hora):
            # A cada evento se mira si cumple con el rango de tempo de cada género.
            # Si es así, se agrega a la lista de eventos en el mapa de géneros.
            if e["tempo"] >= 60 and e["tempo"] <= 90:
                if mp.contains(mapa_generos, "Reggae"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Reggae"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Reggae", nueva_lista_eventos)

            if e["tempo"] >= 70 and e["tempo"] <= 100:
                if mp.contains(mapa_generos, "Down-tempo"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Down-tempo"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Down-tempo", nueva_lista_eventos)

            if e["tempo"] >= 90 and e["tempo"] <= 120:
                if mp.contains(mapa_generos, "Chill-out"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Chill-out"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Chill-out", nueva_lista_eventos)

            if e["tempo"] >= 85 and e["tempo"] <= 115:
                if mp.contains(mapa_generos, "Hip-hop"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Hip-hop"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Hip-hop", nueva_lista_eventos)

            if e["tempo"] >= 120 and e["tempo"] <= 125:
                if mp.contains(mapa_generos, "Jazz and Funk"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Jazz and Funk"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Jazz and Funk", nueva_lista_eventos)

            if e["tempo"] >= 100 and e["tempo"] <= 130:
                if mp.contains(mapa_generos, "Pop"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Pop"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Pop", nueva_lista_eventos)

            if e["tempo"] >= 60 and e["tempo"] <= 80:
                if mp.contains(mapa_generos, "R&B"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "R&B"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "R&B", nueva_lista_eventos)

            if e["tempo"] >=110 and e["tempo"] <= 140:
                if mp.contains(mapa_generos, "Rock"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Rock"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Rock", nueva_lista_eventos)

            if e["tempo"] >= 100 and e["tempo"] <= 160:
                if mp.contains(mapa_generos, "Metal"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Metal"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Metal", nueva_lista_eventos)

    # Conteo con el número de eventos de todos los géneros
    conteo_total = 0

    # Lista donde se guardarán listas [genero, número de eventos]
    lista_final = lt.newList("ARRAY_LIST")

    # Se recorre el mapa de géneros:
    for genero in lt.iterator(mp.keySet(mapa_generos)):
        lista_eventos = me.getValue(mp.get(mapa_generos, genero))
        # Se obtiene el número de eventos por género
        conteo_genero = lt.size(lista_eventos)
        conteo_total += conteo_genero

        # Se crea la lista para cada género
        lista_genero = lt.newList("ARRAY_LIST")
        lt.addLast(lista_genero, genero)
        lt.addLast(lista_genero, conteo_genero)
        # Se agrega la lista de género a la lista global
        lt.addLast(lista_final, lista_genero)

    # Se ordena la lista de generos y número de eventos, según el número de eventos
    lista_final = SortGeneros(lista_final)
    
    # Se obtiene el género con mayor cantidad de eventos, es decir, el primero
    genero_mayor = lt.firstElement(lt.firstElement(lista_final))
    # Se obtiene la lista de eventos del género con más eventos
    lista_genero_mayor = me.getValue(mp.get(mapa_generos, genero_mayor))

    return lista_final, conteo_total, lista_genero_mayor

def requerimiento5_parte2(catalog, lista_genero_mayor):

    # Se crea un mapa para guardar los track_id y contarlos sin repeticiones
    mapa_final = mp.newMap(maptype="PROBING", loadfactor = 0.5)

    for evento in lt.iterator(lista_genero_mayor):
        cancion = evento["track_id"]
        mp.put(mapa_final, cancion, "Valentina - Daniel")
    
    # Se obtiene la cantidad de pistas únicas
    tamaño_mapa = mp.size(mapa_final)

    # ALEATORIEDAD:

    # Se obtiene el tamaño de la lista
    tamaño_lista = lt.size(lista_genero_mayor) 

    # Se obtiene una lista con diez números aleatorios diferentes 
    # que estén dentro del rango del tamaño 
    lista_diez_aleatorios = random.sample(range(tamaño_lista), 10)

    # Se crea una lista para guardar listas [track_id, promedio, cantidad_hashtags]
    lista_final = lt.newList()

    # Se agregan diez eventos aleatorios a la lista
    for i in lista_diez_aleatorios:
        evento_aleatorio = lt.getElement(lista_genero_mayor, i)
        cancion = evento_aleatorio["track_id"]
        # Se llama a GetVaderProm para obtener el número de hashtags y el promedio Vader
        promedio, cantidad_hashtags = GetVaderProm(catalog, cancion)
        lista_cancion = lt.newList()
        lt.addLast(lista_cancion, cancion)
        lt.addLast(lista_cancion, promedio)
        lt.addLast(lista_cancion, cantidad_hashtags)
        lt.addLast(lista_final, lista_cancion)

    lista_final = SortByHashtags(lista_final)

    return lista_final, tamaño_mapa

def GetVaderProm(catalog, cancion):
    """
    Obtiene el promedio de los vader_avg de los hashtags y 
    la cantidad de hashtags de una canción.
    Método: obtiene los vader_avg de los hashtags (sin repeticiones)
    de una canción y los promedia.
    """
    # Busca los hashtags de la canción
    mapa_hashtags = me.getValue(mp.get(catalog["track_id"], cancion))
    lista_hashtags = mp.keySet(mapa_hashtags)
    cantidad_hashtags = lt.size(lista_hashtags)

    promedio = 0

    # Por cada hashtag de la canción, busca el vader en el mapa de hashtags y lo suma
    for hashtag in lt.iterator(lista_hashtags):
        vader = mp.get(catalog["hashtag"], hashtag)
        # Incongruencia entre archivos
        if vader != None:
            promedio += me.getValue(vader)

    promedio /= lt.size(lista_hashtags)

    return round(promedio, 1), cantidad_hashtags


# Funciones de ordenamiento

#5.1
def SortGeneros (lista):
    """
    Toma la lista de listas [genero, eventos_genero] y ordena 
    de mayor de a menor eventos_genero
    """
    return mg.sort(lista, cmpEventosGenero)

#5.2
def SortByHashtags (lista):
    """
    Toma la lista de listas [track_id, promedio, cantidad_hashtags] y ordena 
    de mayor de a menor eventos_genero
    """
    return mg.sort(lista, cmpHashtags)


# Funciones utilizadas para comparar elementos dentro de una lista

#5.1
def cmpEventosGenero (lista1, lista2):
    """
    Compara dos listas [genero, eventos_genero] por eventos_genero
    """
    return lt.lastElement(lista1) > lt.lastElement(lista2)  

#5.2
def cmpHashtags (lista1, lista2):
    """
    Compara dos listas [track_id, promedio, cantidad_hashtags] por 
    cantidad_hashtags
    """
    return lt.lastElement(lista1) > lt.lastElement(lista2)
    