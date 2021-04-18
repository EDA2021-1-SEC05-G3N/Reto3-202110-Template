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
        #caracteristica = "instrumentalness"
        menor = float(input("Ingrese el rango menor: "))
        mayor = float(input("Ingrese el rango mayor: "))
        respuesta = controller.requerimiento1(catalog, menor, mayor, caracteristica)
        print("Total of reproduction: "+str(respuesta[0])+" Total of unique artists: "+str(respuesta[1]))
        print("Se ejecuto el requerimiento 1\n")
    elif int(inputs[0]) == 4:
        menor1 = float(input("Ingrese el rango menor de Energy: "))
        mayor1 = float(input("Ingrese el rango mayor de Energy: "))
        menor2 = float(input("Ingrese el rango menor de Danceability: "))
        mayor2 = float(input("Ingrese el rango mayor de Danceability: "))
        menor1, mayor1, menor2, mayor2 = 0.5, 0.75, 0.75, 1 
        respuesta = controller.requerimiento2(catalog, menor1, mayor1, menor2, mayor2)
        print(respuesta)
        #print("Total of reproduction: "+str(respuesta[0])+" Total of unique artists: "+str(respuesta[1]))
        print("Se ejecuto el requerimiento 2\n")
    elif int(inputs[0]) == 5:
        print("Se ejecuto el requerimiento 3")
    elif int(inputs[0]) == 6:
        print("Se ejecuto el requerimiento 4")
    elif int(inputs[0]) == 7:
        print("Se ejecuto el requerimiento 5")
    else:
        sys.exit(0)
sys.exit(0)
