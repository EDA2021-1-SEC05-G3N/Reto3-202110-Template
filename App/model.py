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

                "track_id": None,
                "hashtag": None
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
    catalog["artist_id"] = mp.newMap()

    catalog["time"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)

    catalog["track_id"] = mp.newMap()
    catalog["hashtag"] = mp.newMap()

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

"""
def addArtista(catalog, evento):

    artista = evento["artist_id"]
"""

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
    lt.addLast(caracter_values['eventos'], evento)
 
def newValorCaracteristica(ValorCaracteristica, CARACTERISTICA):
    """
    Esta función crea la estructura de eventos asociados
    a una característica.
    """
    entry = {CARACTERISTICA: "", "eventos": None}
    entry[CARACTERISTICA] = ValorCaracteristica
    entry['eventos'] = lt.newList('ARRAY_LIST')
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
    mp.put(hashtags['eventos'], evento["hashtag"], None) 
 
def newTrack(track_id):
    
    entry = {'track_id': "", "eventos": None}
    entry['track_id'] = track_id
    entry['eventos'] = mp.newMap()
    return entry


def addHashtag(catalog, evento):

    hashtag_map = catalog['hashtag']
 
    hashtag = evento['hashtag']

    existhashtag = mp.contains(hashtag_map, hashtag)

    if not existhashtag:
        hashtags = newHashtag(evento)
        mp.put(hashtag_map, hashtag, hashtags)

def newHashtag(evento):
    
    entry = {'hashtag': "", "vader_avg": None}
    entry['hashtag'] = evento["hashtag"]
    entry['vader_avg'] = evento["vader_avg"]
    return entry


# Funciones de consulta

def sizeList(catalog, lista):
    tamaño = lt.size(catalog[lista])
    return tamaño

def sizeMap(catalog, mapa):
    tamaño = mp.size(catalog[mapa])
    return tamaño

def r():
    a = "fd"
    return a

def indexHeight(catalog):
    """
    Altura del árbol
    """
    return om.height(catalog['instrumentalness'])

def indexSize(catalog):
    """
    Número de elementos en el índice
    """
    return om.size(catalog['instrumentalness'])

def minKey(catalog):
    """
    Llave más pequeña
    """
    return om.minKey(catalog['instrumentalness'])

def maxKey(catalog):
    """
    Llave más grande
    """
    return om.maxKey(catalog['instrumentalness'])


# Funciones de requerimientos

def requerimiento1(catalog, menor, mayor, caracteristica):

    mapa = om.newMap('RBT')
    # Mapa donde se guardan los artistas sin repeticiones

    lst = om.values(catalog[caracteristica], menor, mayor)
    # Lista de listas de eventos que cumplen con el rango de la característica

    # Se recorre la lista de listas, contando el total de eventos y añadiendo los
    # artistas al mapa, el valor se eligió al azar
    eventos = 0
    for lstdate in lt.iterator(lst):
        eventos += lt.size(lstdate['eventos'])
        for e in lt.iterator(lstdate['eventos']):
            om.put(mapa, e['artist_id'], "Maria José")
    tamaño_mapa = om.size(mapa)

    return eventos, tamaño_mapa, mapa


def requerimiento2(catalog, menor1, mayor1, menor2, mayor2):
    """
    """
    # Se crea un mapa donde se guardan las canciones que cumplen con el rango 
    # de energy, el valor es una tupla con el energy
    mapa_energy = om.newMap('RBT')
    lst = om.values(catalog['energy'], menor1, mayor1)

    for lstdate in lt.iterator(lst):
        for e in lt.iterator(lstdate['eventos']):
            om.put(mapa_energy, e['track_id'], (e['energy'], e['danceability']))
    #mapa_energy = {"1c8b0f2a8d7b1af0ed5af2fcd6f084e1": (0.65, 0.78)}

    canciones = om.keySet(mapa_energy)
    #canciones = ["34234532fgfdgfdhg45., esfsadfsdafsadf3455, ..."]

    seleccionadas = om.newMap('RBT')
    for cancion in lt.iterator(canciones):
        energy = (me.getValue(om.get(mapa_energy, cancion)))[0]
        dance = (me.getValue(om.get(mapa_energy, cancion)))[1]
        if dance <= mayor2 and dance >= menor2:
            om.put(seleccionadas, cancion, (energy, dance))
    #seleccionadas = {"1c8b0f2a8d7b1af0ed5af2fcd6f084e1": (0.65, 0.78)}
   
    # Se obtiene el tamaño del mapa
    tamaño = om.size(seleccionadas) 
    # Se obtiene una lista con cinco números aleatorios diferentes 
    # que estén dentro del rango del tamaño 
    lista_cinco_aleatorios = random.sample(range(tamaño), 5)

    # Se crea un mapa para guardar las llaves aleatorias y sus valores
    mapa_aleatorias = om.newMap('RBT')
    for i in lista_cinco_aleatorios:
        llave_aleatoria = om.select(seleccionadas, i)
        valor = me.getValue(om.get(mapa_energy, llave_aleatoria))
        om.put(mapa_aleatorias, llave_aleatoria, valor)

    return tamaño, mapa_aleatorias


def requerimiento3(catalog, menor1, mayor1, menor2, mayor2):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    mapa_instrumentalness = om.newMap('RBT')
    lst = om.values(catalog['instrumentalness'], menor1, mayor1)

    for lstdate in lt.iterator(lst):
        for e in lt.iterator(lstdate['eventos']):
            om.put(mapa_instrumentalness, e['track_id'], (e['instrumentalness'], e['tempo']))

    canciones = om.keySet(mapa_instrumentalness)

    seleccionadas = om.newMap('RBT')
    for cancion in lt.iterator(canciones):
        instrumental = (me.getValue(om.get(mapa_instrumentalness, cancion)))[0]
        tempo = (me.getValue(om.get(mapa_instrumentalness, cancion)))[1]
        if tempo <= mayor2 and tempo >= menor2:
            om.put(seleccionadas, cancion, (instrumental, tempo))

    tamaño = om.size(seleccionadas) 

    mapa_aleatorias = om.newMap('RBT')

    lista_cinco_aleatorios = random.sample(range(tamaño), 5)

    for i in lista_cinco_aleatorios:
        llave_aleatoria = om.select(seleccionadas, i)
        valor = me.getValue(om.get(mapa_instrumentalness, llave_aleatoria))
        om.put(mapa_aleatorias, llave_aleatoria, valor)

    return tamaño, mapa_aleatorias


def requerimiento4(catalog, mapa_generos):

    eventos_total = 0

    for i in lt.iterator(om.keySet(mapa_generos)):

        menor = me.getValue(om.get(mapa_generos, i))[0]
        mayor = me.getValue(om.get(mapa_generos, i))[1]
        eventos, tamaño_mapa, mapa = requerimiento1(catalog, menor, mayor, 'tempo')
        om.put(mapa_generos, i, (eventos, tamaño_mapa,  mapa, menor, mayor))
        eventos_total += eventos

    return mapa_generos, eventos_total


def requerimiento5_parte1(catalog, horamin, horamax):

    lista_horas =  om.values(catalog['time'], horamin, horamax)
    mapa_generos = mp.newMap(numelements= 10)

    conteo_total, conteo_0, conteo_1, conteo_2, conteo_3 = 0, 0, 0, 0, 0
    conteo_4, conteo_5, conteo_6, conteo_7, conteo_8 = 0, 0, 0, 0, 0


    for lst in lt.iterator(lista_horas):
        for e in lt.iterator(lst['eventos']):
            
            if e["tempo"] >= 60 and e["tempo"] <= 90:
                if mp.contains(mapa_generos, "Reggae"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Reggae"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Reggae", nueva_lista_eventos)
                conteo_0 += 1

            if e["tempo"] >= 70 and e["tempo"] <= 100:
                if mp.contains(mapa_generos, "Down-tempo"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Down-tempo"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Down-tempo", nueva_lista_eventos)
                conteo_1 += 1

            if e["tempo"] >= 90 and e["tempo"] <= 120:
                if mp.contains(mapa_generos, "Chill-out"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Chill-out"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Chill-out", nueva_lista_eventos)
                conteo_2 += 1

            if e["tempo"] >= 85 and e["tempo"] <= 115:
                if mp.contains(mapa_generos, "Hip-hop"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Hip-hop"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Hip-hop", nueva_lista_eventos)
                conteo_3 += 1

            if e["tempo"] >= 120 and e["tempo"] <= 125:
                if mp.contains(mapa_generos, "Jazz and Funk"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Jazz and Funk"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Jazz and Funk", nueva_lista_eventos)
                conteo_4 += 1

            if e["tempo"] >= 100 and e["tempo"] <= 130:
                if mp.contains(mapa_generos, "Pop"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Pop"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Pop", nueva_lista_eventos)
                conteo_5 += 1

            if e["tempo"] >= 60 and e["tempo"] <= 80:
                if mp.contains(mapa_generos, "R&B"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "R&B"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "R&B", nueva_lista_eventos)
                conteo_6 += 1

            if e["tempo"] >=110 and e["tempo"] <= 140:
                if mp.contains(mapa_generos, "Rock"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Rock"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Rock", nueva_lista_eventos)
                conteo_7 += 1

            if e["tempo"] >= 100 and e["tempo"] <= 160:
                if mp.contains(mapa_generos, "Metal"):
                    lista_eventos = me.getValue(mp.get(mapa_generos, "Metal"))
                    lt.addLast(lista_eventos, e)
                else:
                    nueva_lista_eventos = lt.newList("ARRAY_LIST")
                    mp.put(mapa_generos, "Metal", nueva_lista_eventos)
                conteo_8 += 1

    conteo_total = conteo_0 + conteo_1 + conteo_2 + conteo_3 + conteo_4 
    conteo_total += conteo_5 + conteo_6 + conteo_7 + conteo_8        

    lista_final = lt.newList('ARRAY_LIST')
    for i in range(9):
        if i == 0:
            genero = "Reggae"
            conteo = conteo_0
        elif i == 1:
            genero = "Down-tempo"
            conteo = conteo_1
        elif i == 2:
            genero = "Chill-out"
            conteo = conteo_2
        elif i == 3:
            genero = "Hip-hop"
            conteo = conteo_3
        elif i == 4:
            genero = "Jazz and Funk"
            conteo = conteo_4
        elif i == 5:
            genero = "Pop"
            conteo = conteo_5
        elif i == 6:
            genero = "R&B"
            conteo = conteo_6
        elif i == 7:
            genero = "Rock"
            conteo = conteo_7
        elif i == 8:
            genero = "Metal"
            conteo = conteo_8

        lista_pequeña = lt.newList("ARRAY_LIST")
        lt.addLast(lista_pequeña, genero)
        lt.addLast(lista_pequeña, conteo)
        lt.addLast(lista_final, lista_pequeña)

    #Se ordena la lista de generos y número de eventos
    lista_final = SortGeneros(lista_final)
    
    #Se saca la lista de eventos del género con mayor eventos
    genero_mayor = lt.firstElement(lt.firstElement(lista_final))
    lista_genero_mayor = me.getValue(mp.get(mapa_generos, genero_mayor))

    return lista_final, conteo_total, lista_genero_mayor

"""
def requerimiento5_parte2_ANTES(catalog, lista_genero_mayor):
    
    mapa_final = mp.newMap()


    for e in lt.iterator(lista_genero_mayor):
        cancion = e["track_id"]
        promedio, cantidad_hashtags = GetVaderProm(catalog, cancion)
        mp.put(mapa_final, cancion, (promedio, cantidad_hashtags))

    print(mp.size(mapa_final))

    return mapa_final
"""

def requerimiento5_parte2(catalog, lista_genero_mayor):
    
    print(lt.size(lista_genero_mayor))

    lista_prueba1 = []
    lista_prueba2 = lt.newList()

    for e in lt.iterator(lista_genero_mayor):
        if e["track_id"] not in lista_prueba1:
            lista_prueba1.append(e["track_id"])
        if lt.isPresent(lista_prueba2, e["track_id"]) == False:
            lt.addLast(lista_prueba2, e["track_id"])
        
    print(len(lista_prueba1))
    print(lista_prueba1 )
    print(lt.size(lista_prueba2))
    #print(lista_genero_mayor)



    # Se crea un mapa para guardar los track_id y contar sin repeticiones
    mapa_final = mp.newMap()

    for e in lt.iterator(lista_genero_mayor):
        cancion = e["track_id"]
        mp.put(mapa_final, cancion, "Hola")
    
    tamaño_mapa = mp.size(mapa_final)


    # Se obtiene el tamaño de la lista
    tamaño_lista = lt.size(lista_genero_mayor) 

    # Se obtiene una lista con diez números aleatorios diferentes 
    # que estén dentro del rango del tamaño 
    lista_diez_aleatorios = random.sample(range(tamaño_lista), 10)

    # Se crea una lista para guardar listas [track_id, promedio, cantidad_hashtags]
    lista_final = lt.newList()

    # Se agregan diez eventos aleatorios a la lista
    for i in lista_diez_aleatorios:
        e_aleatorio = lt.getElement(lista_genero_mayor, i)
        cancion = e_aleatorio["track_id"]
        promedio, cantidad_hashtags = GetVaderProm(catalog, cancion)
        lista_pequeña = lt.newList()
        lt.addLast(lista_pequeña, cancion)
        lt.addLast(lista_pequeña, promedio)
        lt.addLast(lista_pequeña, cantidad_hashtags)
        lt.addLast(lista_final, lista_pequeña)

    lista_final = SortByHashtags(lista_final)

    return lista_final, tamaño_mapa

def GetVaderProm(catalog, cancion):
    """
    Obtiene el promedio de los vader_avg de los hashtags de una canción.
    """
    
    #Busca los hashtags de la canción
    mapa_hashtags = me.getValue(mp.get(catalog["track_id"], cancion))
    lista_hashtags = mp.keySet(mapa_hashtags["eventos"])
    cantidad_hashtags = lt.size(lista_hashtags)
    promedio = 0

    for h in lt.iterator(lista_hashtags):
        a = mp.get(catalog["hashtag"], h)
        if a != None:
            promedio += me.getValue(a)["vader_avg"]

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