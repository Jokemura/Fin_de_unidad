import csv
import pandas as pd
from csv import writer
import os
os.system("cls")

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' 
RESET = '\033[39m'

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
                if opcion == 1 and libro["editorial"] == palabra:
                        print(GREEN + libro["titulo"] + RESET)
                elif opcion == 2 and libro["genero"] == palabra:
                        print(GREEN + libro["titulo"] + RESET)                
                for autor in autores:
                    if opcion == 3 and autor == palabra:
                            print(GREEN + libro["titulo"] + RESET)
                   
    def numeroAutores(self, cant_autores): #Opcion 8
        with open("D:/Silabuz/CondicionalesBucles/libros.csv","r") as file:
            reader = csv.DictReader(file)
            #reader es iterable          
            for libro in reader:
                autores = libro["autores"].split("-")
                if len(autores) == cant_autores:    
                    print(GREEN + libro["titulo"] + RESET)  
                 
    def actualizarDatos(self, id, item, palabra): #Opcion 9
        if item == "titulo":
            data = pd.read_csv("D:/Silabuz/CondicionalesBucles/libros.csv")
            data.iat[id, 1] = palabra
            data.to_csv("D:/Silabuz/CondicionalesBucles/libros.csv", index=False)
            print(GREEN + "Se realizo el cambio con exito"+ RESET)
        elif item == "genero":
            data = pd.read_csv("D:/Silabuz/CondicionalesBucles/libros.csv")
            data.iat[id, 2] = palabra
            data.to_csv("D:/Silabuz/CondicionalesBucles/libros.csv", index=False)
            print(GREEN + "Se realizo el cambio con exito"+ RESET)
        elif item == "isbn":
            data = pd.read_csv("D:/Silabuz/CondicionalesBucles/libros.csv")
            data.iat[id, 3] = palabra
            data.to_csv("D:/Silabuz/CondicionalesBucles/libros.csv", index=False)
            print(GREEN + "Se realizo el cambio con exito"+ RESET)           
        elif item == "editorial":
            data = pd.read_csv("D:/Silabuz/CondicionalesBucles/libros.csv")
            data.iat[id, 4] = palabra
            data.to_csv("D:/Silabuz/CondicionalesBucles/libros.csv", index=False)
            print(GREEN + "Se realizo el cambio con exito"+ RESET)            
        elif item == "autores":
            data = pd.read_csv("D:/Silabuz/CondicionalesBucles/libros.csv")
            data.iat[id, 5] = palabra
            data.to_csv("D:/Silabuz/CondicionalesBucles/libros.csv", index=False)
            print(GREEN + "Se realizo el cambio con exito"+ RESET)

         

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
            print("-"*60)
            print(YELLOW +"Ingrese solamente el numero de la opcion a buscar: "+ RESET)           
            print(YELLOW + "Opcion 1: Editorial\nOpcion 2: Genero\nOpcion 3: Autor" + RESET)
            print("-"*60)
            opcion = int(input("Ingrese el numero de la opcion que desea buscar:  "))
            print("-"*60)
            palabra = input("Ingrese la palabra a buscar: ")  
            print("-"*60)          
            libro = Libro(0, "", "", "", "","")
            libro.buscarLibro(opcion, palabra.lower())            
            break
        case '8':
            print("-"*60)
            cant_autores = int(input(YELLOW + "Ingrese cantidad de autores: "+ RESET))
            print("-"*60)
            libro = Libro(0, "", "", "", "","")
            libro.numeroAutores(cant_autores)
            break
        case '9':
            print("-"*60)
            id = int(input(YELLOW +"Ingrese el id del libro que desea editar: "+ RESET))
            print("-"*60)
            item = input(YELLOW +"Ingrese el atributo que desea cambiar: "+ RESET)
            print("-"*60)
            palabra = input("Ingrese la data a actualizar: ")
            libro = Libro(0, "", "", "", "","")
            libro.actualizarDatos(id,item, palabra)
            break
        case '10':
            print("hola10")
            break
