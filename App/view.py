﻿"""
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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- : Caracterizar las reproducciones ")
    print("2- : Encontrar música para festejar ")
    print("3- : Encontrar música para estudiar ")
    print("4- : Estimar las reproducciones de los géneros musicales ")
    print("5- : : Indicar el género musical más escuchado en un tiempo ")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
    elif int(inputs[0]) == 1:
        print("Se ejecuto el requerimiento 1")
    elif int(inputs[0]) == 2:
        print(("Se ejecuto el requerimiento 2")
    elif int(inputs[0]) == 3:
        print("Se ejecuto el requerimiento 3")
    elif int(inputs[0]) == 4:
        print("Se ejecuto el requerimiento 4")
    elif int(inputs[0]) == 5:
        print("Se ejecuto el requerimiento 5")
    else:
        sys.exit(0)
sys.exit(0)
