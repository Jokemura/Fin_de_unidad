menu = True
while menu == True:
    print("---------------------------------------------------------")
    print("-                   POKEAPI                             -")
    print("---------------------------------------------------------")
    print("-                MENU DE OPCIONES                       -")
    print("---------------------------------------------------------")
    print("1| Listar pokemons por generación                       -")
    print("2| Listar pokemons por forma                            -")
    print("3| Listar pokemons por habilidad                        -")
    print("4| Listar pokemons por habitat                          -")
    print("5| Listar pokemons por tipo                             -")
    print("---------------------------------------------------------")
    opc = input("Ingresa opcion: ")

    while opc not in ('1', '2', '3', '4', '5'):
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

