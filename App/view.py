"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
import model
import datetime


"""
La vista se encarga de la interacción con el usuario
Presenta el menú de opciones y por cada selección
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el catálogo")
    print("3- Req. 1: Caracterizar las reproducciones")
    print("4- Req. 2: Encontrar música para festejar")
    print("5- Req. 3: Encontrar música para estudiar")
    print("6- Req. 4: Estimar las reproducciones de los géneros musicales")
    print("7- Req. 5: Indicar el género musical más escuchado en un tiempo")

def initCatalog():
    """
    Inicializa el catálogo de eventos
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los datos en la estructura de datos
    """
    return controller.loadData(catalog)

def printResults(lista_eventos, sample=5):
    size = lt.size(lista_eventos)
    if(size > sample):
        print("\n-Los primeros 5 eventos cargados son: ")
        i = 1
        while i <= sample:
            evento = lt.getElement(lista_eventos, i)
            print("\nEvento # "+str(i))
            print("id del evento: "+str(evento["id"]))
            print("id del user: "+str(evento["user_id"]))
            print("id de la canción: "+str(evento["track_id"]))
            print("instrumentalness: "+str(evento["instrumentalness"]))
            print("danceability: "+str(evento["danceability"]))
            print("tempo: "+str(evento["tempo"]))
            i+=1
        print("\nLos últimos 5 eventos cargados son: ")
        i = -4
        while i < 1:
            evento = lt.getElement(lista_eventos, i)
            print("\nEvento # "+str(size + i))
            print("id del evento: "+str(evento["id"]))
            print("id del user: "+str(evento["user_id"]))
            print("id de la canción: "+str(evento["track_id"]))
            print("instrumentalness: "+str(evento["instrumentalness"]))
            print("danceability: "+str(evento["danceability"]))
            print("tempo: "+str(evento["tempo"]))
            i+=1

def printReq1(menor, mayor, respuesta):
    print('\n++++++ Req No. 1 results... +++++')
    print('Instrumentalness is between '+str(menor)+' and '+str(mayor))
    print("Total of reproduction: "+str(respuesta[0])+" Total of unique artists: "+str(respuesta[1]))

def printReq2_3(menor1, mayor1, menor2, mayor2, numero, mapa, req):

    if req == 2:
        parametro1 = 'Energy'
        parametro2 = 'Danceability'
    else:
        parametro1 = 'Instrumentalness'
        parametro2 = 'Tempo'

    print('\n++++++ Req No. '+str(req)+' results... ++++++')
    print(parametro1+' is between '+str(menor1)+' and '+str(mayor1))
    print(parametro2+' is between '+str(menor2)+' and '+str(mayor2))
    print('Total of unique tracks in events: '+str(numero)+"\n")

    print('--- Unique track_id ---')
    lista_llaves = om.keySet(mapa)
    n = 1
    for llave in lt.iterator(lista_llaves):
        valor = me.getValue(om.get(mapa, llave))
        print('Track '+str(n)+': '+str(llave)+' with '+parametro1.lower()+' of '+str(valor[0])+' and '+parametro2.lower()+' of '+str(valor[1]))
        n += 1

def crear_mapa_generos (cantidad_generos, nuevo_genero):
    mapa_generos = om.newMap()

    for i in range(cantidad_generos):
        if i == cantidad_generos-1 and (nuevo_genero in "sísiSíSiSISÍ"):
            nuevo = input("Ingrese el género musical nuevo: ")
            menor = float(input("Ingrese el rango menor de Tempo: "))
            mayor = float(input("Ingrese el rango mayor de Tempo: "))
        else:
            nuevo = input("Ingrese el género musical #"+str(i+1)+": ")

            if nuevo == "Reggae":
                menor, mayor = 60, 90
            elif nuevo == "Down-tempo":
                menor, mayor = 70, 100
            elif nuevo == "Chill-out":
                menor, mayor = 90, 120
            elif nuevo == "Hip-hop":
                menor, mayor = 85, 115
            elif nuevo == "Jazz and Funk":
                menor, mayor = 120, 125
            elif nuevo == "Pop":
                menor, mayor = 100, 130
            elif nuevo == "R&B":
                menor, mayor = 60, 80
            elif nuevo == "Rock":
                menor, mayor = 110, 140
            elif nuevo == "Metal":
                menor, mayor = 100, 160
        
        om.put(mapa_generos, nuevo, (menor, mayor))

    return mapa_generos

def printReq4 (respuesta):
    print('\n++++++ Req No. 4 results... +++++\n'+'Total of reproductions: '+str(respuesta[1]))
    for i in lt.iterator(om.keySet(respuesta[0])):
        eventos, tamaño_mapa, mapa, menor, mayor = me.getValue(om.get(mapa_generos, i))
        print("\n========"+" "+i+" "+"========")
        print("For "+i+" the tempo is between "+str(menor)+" and "+str(mayor)+" BPM")
        print(i+" reproductions: "+str(eventos)+" with "+str(tamaño_mapa)+" different artists")
        print("-----"+" Some artists for "+i+" "+"-----")
        n = 1
        for artista in lt.iterator(om.keySet(mapa)):
            print('Artist '+str(n)+': '+str(artista))
            n += 1
            if n == 11:
                break

def printReq5 (respuesta, horamin, horamax):
    print("\n++++++ Req No. 5 results... ++++++")
    print("There is a total of "+str(respuesta[0][1])+" reproductions between "+str(horamin)+" and "+str(horamax))
    print("====================== GENRES SORTED REPRODUCTIONS ======================")
    for i in range(1,10):
        lista_pequeña = lt.getElement(respuesta[0][0], i)
        #print(lista_pequeña)
        genero = lt.firstElement(lista_pequeña)
        eventos = lt.lastElement(lista_pequeña)
        print("TOP "+str(i)+": "+str(genero)+" with "+str(eventos)+" reps")
    lista_mayor = lt.firstElement(respuesta[0][0])
    genero_mayor = lt.firstElement(lista_mayor)
    eventos_mayor = lt.lastElement(lista_mayor)
    print("\nThe TOP GENRE is "+str(genero_mayor)+" with "+str(eventos_mayor)+" reproductions...\n")

    print("========================== "+str(genero_mayor)+" SENTIMENT ANALYSIS =========================")
    print(str(genero_mayor)+" has "+str(respuesta[1][1])+" unique tracks...")
    print("The first TOP 10 tracks are...\n")
    
    i = 0
    for cada_lista in lt.iterator(respuesta[1][0]):
        cancion = lt.getElement(cada_lista, 1)
        promedio = lt.getElement(cada_lista, 2)
        hashtags = lt.getElement(cada_lista, 3)
        i += 1
        print("TOP "+str(i)+" track: "+str(cancion)+" with hashtags "+str(hashtags)+
            " and VADER = "+str(promedio))


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # catalog es el controlador que se usará de acá en adelante
        catalog = controller.initCatalog()
        
    elif int(inputs[0]) == 2:
        print("\nCargando información de eventos ....")
        controller.loadData(catalog)
        print('\n-Eventos cargados: ' + str(controller.sizeList(catalog, "eventos")))
        print('\n-Canciones únicas: ' + str(controller.sizeMap(catalog, "track_id")))
        printResults(catalog["eventos"])
        print('\n-Artistas únicos: ' + str(controller.sizeMap(catalog, "artist_id")))


    elif int(inputs[0]) == 3:
        caracteristica = input("Ingrese la característica: ")
        menor = float(input("Ingrese el rango menor: "))
        mayor = float(input("Ingrese el rango mayor: "))
        #
        caracteristica, menor, mayor = 'instrumentalness', 0.75, 1.0
        #
        respuesta = controller.requerimiento1(catalog, menor, mayor, caracteristica)

        printReq1(menor, mayor, respuesta[2])
        print("Tiempo [ms]: ", f"{respuesta[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{respuesta[1]:.3f}")
        print("\nSe ejecutó el requerimiento 1\n")


    elif int(inputs[0]) == 4:
        menor1 = float(input("Ingrese el rango menor de Energy: "))
        mayor1 = float(input("Ingrese el rango mayor de Energy: "))
        menor2 = float(input("Ingrese el rango menor de Danceability: "))
        mayor2 = float(input("Ingrese el rango mayor de Danceability: "))
        #
        menor1, mayor1, menor2, mayor2 = 0.5, 0.75, 0.75, 1 
        #
        respuesta = controller.requerimiento2(catalog, menor1, mayor1, menor2, mayor2)
        
        printReq2_3(menor1, mayor1, menor2, mayor2, respuesta[2][0], respuesta[2][1], 2)
        print("Tiempo [ms]: ", f"{respuesta[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{respuesta[1]:.3f}")
        print("\nSe ejecutó el requerimiento 2\n")


    elif int(inputs[0]) == 5:
        menor1 = float(input("Ingrese el rango menor de Instrumentalness: "))
        mayor1 = float(input("Ingrese el rango mayor de Instrumentalness: "))
        menor2 = float(input("Ingrese el rango menor de Tempo: "))
        mayor2 = float(input("Ingrese el rango mayor de Tempo: "))
        #
        menor1, mayor1, menor2, mayor2 = 0.6, 0.9, 40.0, 60.0 
        #
        respuesta = controller.requerimiento3(catalog, menor1, mayor1, menor2, mayor2)
        
        printReq2_3(menor1, mayor1, menor2, mayor2, respuesta[2][0], respuesta[2][1], 3)
        print("Tiempo [ms]: ", f"{respuesta[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{respuesta[1]:.3f}")
        print("\nSe ejecutó el requerimiento 3\n")


    elif int(inputs[0]) == 6:   
        cantidad_generos = int(input("¿Cuántos generos desea buscar? "))
        nuevo_genero = input("¿Desea añadir un nuevo género? ")
        mapa_generos = crear_mapa_generos(cantidad_generos, nuevo_genero)

        respuesta = controller.requerimiento4(catalog, mapa_generos)
        printReq4(respuesta[2])
        print("Tiempo [ms]: ", f"{respuesta[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{respuesta[1]:.3f}")

        print("\nSe ejecutó el requerimiento 4\n")


    elif int(inputs[0]) == 7:
        #horamin = datetime.datetime.strptime((input("Ingrese el valor mínimo de la hora: ")), '%H:%M:%S').time()
        #horamax = datetime.datetime.strptime((input("Ingrese el valor máximo de la hora: ")), '%H:%M:%S').time()
        #
        horamin = datetime.datetime.strptime("7:15:00", '%H:%M:%S').time()
        horamax = datetime.datetime.strptime("9:45:00", '%H:%M:%S').time()
        #
        
        #print(mp.keySet((catalog["track_id"])))
        respuesta = controller.requerimiento5(catalog, horamin, horamax)
        #print(respuesta[1])
        printReq5(respuesta[2], horamin, horamax)
        print("Tiempo [ms]: ", f"{respuesta[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{respuesta[1]:.3f}")

        print("\nSe ejecutó el requerimiento 5\n")
    else:
        sys.exit(0)
sys.exit(0)
