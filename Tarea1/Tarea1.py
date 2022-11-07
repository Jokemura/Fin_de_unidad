from Libro import *
from Colors import *

menu = True


def volerMenu():
    print(YELLOW + "--------------------------------------")
    print(" Press una tecla para voler al menu  -")
    print("--------------------------------------" + RESET)
    input()
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
            Libro.leerCsv()
            volerMenu()
        case '2':
            Libro.listarlibros()

        case '3':
            Libro.agregarLibros()
            # break
        case '4':
            Libro.eliminar()
            #break
        case '5':
            Libro.buscar_libro()
            #break
        case '6':
            Libro.ordenar_titulos()
            #break
        case '7':
            Libro.buscarLibros()
            #break
        case '8':
            Libro.numeroAutores()
            #break
        case '9':
            print("hola9")
            break
        case '10':
            print("hola10")
            break
