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
assert cf
import random

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
#11
    catalog = {'instrumentalness': None,
                'liveness': None,
                "speechiness": None,
                "danceability": None,
                "valence": None,
                "loudness": None,
                "tempo": None,
                "acousticness": None,
                "energy": None,
                "mode": None,
                "key": None
                }

    catalog['instrumentalness'] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog['liveness'] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["speechiness"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["danceability"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["valence"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["loudness"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["tempo"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["acousticness"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["energy"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["mode"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    catalog["key"] = om.newMap(omaptype='RBT',
                                      comparefunction=None)
    return catalog


# Funciones para agregar informacion al catalogo

def addEvento(catalog, evento):

    addEventoInstrumentalness1(catalog, evento, 'instrumentalness')
    addEventoInstrumentalness1(catalog, evento, 'liveness')
    addEventoInstrumentalness1(catalog, evento, 'speechiness')
    addEventoInstrumentalness1(catalog, evento, 'danceability')
    addEventoInstrumentalness1(catalog, evento, 'valence')
    addEventoInstrumentalness1(catalog, evento, 'loudness')
    addEventoInstrumentalness1(catalog, evento, 'tempo')
    addEventoInstrumentalness1(catalog, evento, 'acousticness')
    addEventoInstrumentalness1(catalog, evento, 'energy')
    addEventoInstrumentalness1(catalog, evento, 'mode')
    addEventoInstrumentalness1(catalog, evento, 'key')
    
"""
def addEventoInstrumentalness(catalog, evento):

    countries_map = catalog['instrumentalness']
 
    pubcountry = evento['instrumentalness']

    existcountry = om.contains(countries_map, pubcountry)

    if existcountry:
        entry = om.get(countries_map, pubcountry)
        country_values = me.getValue(entry)
    else:
        country_values = newCountry(pubcountry)
        om.put(countries_map, pubcountry, country_values)
    lt.addLast(country_values['eventos'], evento) 
 

def newCountry(pubcountry):
    
    entry = {'instrumentalness': "", "eventos": None}
    entry['instrumentalness'] = pubcountry
    entry['eventos'] = lt.newList('ARRAY_LIST')
    return entry
"""



def addEventoInstrumentalness1(catalog, evento, CARACTERISTICA):
    """
    Esta funcion adiciona un video a la lista de videos.
    Los países se guardan en un Map, donde la llave es el país
    y el valor la lista de videos de ese país.
    """

    countries_map = catalog[CARACTERISTICA]
 
    pubcountry = evento[CARACTERISTICA]

    existcountry = om.contains(countries_map, pubcountry)

    if existcountry:
        entry = om.get(countries_map, pubcountry)
        country_values = me.getValue(entry)
    else:
        country_values = newCountry1(pubcountry, CARACTERISTICA)
        om.put(countries_map, pubcountry, country_values)
    lt.addLast(country_values['eventos'], evento) 
 

def newCountry1(pubcountry, CARACTERISTICA):
    """
    Esta funcion crea la estructura de videos asociados
    a un año.
    """
    entry = {CARACTERISTICA: "", "eventos": None}
    entry[CARACTERISTICA] = pubcountry
    entry['eventos'] = lt.newList('ARRAY_LIST')
    return entry


# Funciones de consulta

def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['instrumentalness'])


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['instrumentalness'])


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer['instrumentalness'])


def maxKey(analyzer):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer['instrumentalness'])

def requerimiento1(catalog, menor, mayor, caracteristica):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    mapa = om.newMap('RBT')
    lst = om.values(catalog[caracteristica], menor, mayor)
    eventos = 0
    for lstdate in lt.iterator(lst):
        eventos += lt.size(lstdate['eventos'])
        for e in lt.iterator(lstdate['eventos']):
            om.put(mapa, e['artist_id'], "Maria José")
    tamaño_mapa = om.size(mapa)
    return eventos, tamaño_mapa


def requerimiento2(catalog, menor1, mayor1, menor2, mayor2):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
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
    tamaño = om.size(seleccionadas) 

    mapa_aleatorias = om.newMap('RBT')
    lista_cinco_aleatorios = random.sample(range(tamaño), 5)

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



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
