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
assert cf
import model
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el catálogo")
    print("3- Req. 1: Caracterizar las reproducciones")
    print("4- Req. 2: Encontrar música para festejar")
    print("5- Req. 3: Encontrar música para estudiar")
    print("6- Req. 4: Estimar las reproducciones de los géneros musicales")
    print("7- Req. 5: Indicar el género musical más escuchado en un tiempo")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    return controller.loadData(catalog)

def printReq2_3(menor1, mayor1, menor2, mayor2, numero, mapa):

    print('\n++++++ Req No. 2 results... ++++++')
    print('Energy is between '+str(menor1)+' and '+str(mayor1))
    print('Danceability is between '+str(menor2)+' and '+str(mayor2))
    print('Total of unique tracks in events: '+str(numero)+"\n")

    lista_llaves = om.keySet(mapa)
    n = 1
    for llave in lt.iterator(lista_llaves):
        valor = me.getValue(om.get(mapa, llave))
        print('Track '+str(n)+': '+str(llave)+' with energy of '+str(valor[0])+' and danceability of '+str(valor[1]))
        n += 1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        catalog = controller.initCatalog()
        
    elif int(inputs[0]) == 2:
        print("\nCargando información de eventos ....")
        respuesta = controller.loadData(catalog)
        print('Altura del arbol: ' + str(controller.indexHeight(catalog)))
        print('Elementos en el arbol: ' + str(controller.indexSize(catalog)))
        print('Menor Llave: ' + str(controller.minKey(catalog)))
        print('Mayor Llave: ' + str(controller.maxKey(catalog)))


    elif int(inputs[0]) == 3:
        caracteristica = input("Ingrese la característica: ")
        menor = float(input("Ingrese el rango menor: "))
        mayor = float(input("Ingrese el rango mayor: "))
        #
        caracteristica, menor, mayor = 'instrumentalness', 0.75, 1.0
        #
        respuesta = controller.requerimiento1(catalog, menor, mayor, caracteristica)

        print('\n++++++ Req No. 1 results... +++++')
        print('Instrumentalness is between '+str(menor)+' and '+str(mayor))
        print("Total of reproduction: "+str(respuesta[0])+" Total of unique artists: "+str(respuesta[1]))
        print("\nSe ejecutó el requerimiento 1\n")


    elif int(inputs[0]) == 4:
        menor1 = float(input("Ingrese el rango menor de Energy: "))
        mayor1 = float(input("Ingrese el rango mayor de Energy: "))
        menor2 = float(input("Ingrese el rango menor de Danceability: "))
        mayor2 = float(input("Ingrese el rango mayor de Danceability: "))
        #
        menor1, mayor1, menor2, mayor2 = 0.5, 0.75, 0.75, 1 
        respuesta = controller.requerimiento2(catalog, menor1, mayor1, menor2, mayor2)
        
        printReq2_3(menor1, mayor1, menor2, mayor2, respuesta[0], respuesta[1])
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
        
        printReq2_3(menor1, mayor1, menor2, mayor2, respuesta[0], respuesta[1])
        print("\nSe ejecutó el requerimiento 3\n")


    elif int(inputs[0]) == 6:
        print("Se ejecutó el requerimiento 4")
    elif int(inputs[0]) == 7:
        print("Se ejecutó el requerimiento 5")
    else:
        sys.exit(0)
sys.exit(0)
