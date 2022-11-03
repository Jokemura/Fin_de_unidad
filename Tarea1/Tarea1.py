import csv
import pandas as pd
from csv import writer
import os
os.system("cls")

class Libro:
    def __init__(self, id, titulo, genero, isbn, editorial, autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autores = autores

    def buscarLibro(self, opcion, palabra): #Opcion 7
        with open("D:/Silabuz/CondicionalesBucles/libros.csv","r") as file:
            reader = csv.DictReader(file)
            #reader es iterable
            for libro in reader:
                autores = libro["autores"].split("-")
                if opcion == 1:
                    if libro["editorial"] == palabra:
                        print(libro["titulo"])
                elif opcion == 2:
                    if libro["genero"] == palabra:
                        print(libro["titulo"])
                elif opcion == 3:                   
                    for autor in autores:
                        if autor == palabra:
                            print(libro["titulo"])
                   
    def numeroAutores(self, cant_autores): #Opcion 8
        with open("D:/Silabuz/CondicionalesBucles/libros.csv","r") as file:
            reader = csv.DictReader(file)
            #reader es iterable          
            for libro in reader:
                autores = libro["autores"].split("-")
                if len(autores) == cant_autores:    
                    print(libro["titulo"])
                 
    def actualizarDatos(self): #Opcion 9
        item = 'melon'
        data = pd.read_csv("D:/Silabuz/CondicionalesBucles/libros.csv")
        data.iat[0, 2] = item
        data.to_csv("D:/Silabuz/CondicionalesBucles/libros.csv", index=False)

menu = True
while menu == True:
    print("---------------------------------------------------------")
    print("-                   LIBRERIA                            -")
    print("---------------------------------------------------------")
    print("-                MENU DE OPCIONES                       -")
    print("---------------------------------------------------------")
    print("1| Leer archivo de disco duro                           -")
    print("2| Listar libros                                        -")
    print("3| Agregar libro                                        -")
    print("4| Eliminar libro                                       -")
    print("5| Buscar libro                                         -")
    print("6| Ordenar libros por título                            -")
    print("7| Buscar libros por autor, editorial o género          -")
    print("8| Buscar libros por número de autores                  -")
    print("9| Editar o actualizar datos de un libro                -")
    print("10| Guardar libros en archivo de disco duro             -")
    print("---------------------------------------------------------")
    opc = input("Ingresa opcion: ")

    while opc not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        opc = input("Ingresa opcion: ")

    match opc:
        case '1':
            print("hola1")
            break
        case '2':
            print("hola2")
            break
        case '3':
            print("hola3")
            break
        case '4':
            print("hola4")
            break
        case '5':
            print("hola5")
            break
        case '6':
            print("hola6")
            break
        case '7':
            print("Buscar libros por autor, editorial o género")
            print("Opcion 1: Editorial\nOpcion 2: Genero\nOpcion 3: Autor")
            opcion = int(input("Ingrese el numero de la opcion que desea buscar:  "))
            palabra = input("Ingrese la palabra a buscar: ")            
            libro = Libro(0, "", "", "", "","")
            libro.buscarLibro(opcion, palabra)
            break
        case '8':
            cant_autores = int(input("Ingrese cantidad de autores: "))
            libro = Libro(0, "", "", "", "","")
            libro.numeroAutores(cant_autores)
            break
        case '9':
            print("hola9")
            break
        case '10':
            print("hola10")
            break
