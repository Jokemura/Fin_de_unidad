import json

import requests
from tabulate import tabulate


@staticmethod
def listarGeneracion():
    listaPokemonsGeneracion=[]
    url = "https://pokeapi.co/api/v2/generation/"
    idGeneracion=input("Ingresa la generacion: ")
    res = requests.get(url+idGeneracion)
    data=res.json()
    listaPokemonsGeneracion=data['pokemon_species']
    # print(listaPokemonsGeneracion)
    print("------------------------------------------------------------------------")
    print(f"-             POKEMONES DE LA {idGeneracion}ra GENERACION               -")
    print("------------------------------------------------------------------------")
    
    print(tabulate(listaPokemonsGeneracion, headers="keys", tablefmt='pretty'))


@staticmethod    
def listarForma():
    listaShape=[]
    url = "https://pokeapi.co/api/v2/pokemon-shape/"
    shape=input("Ingresa la Forma de un Pokemon: ")
    res = requests.get(url+shape)
    data=res.json()
    listaShape=data['pokemon_species']
    # print(listaPokemonsGeneracion)
    print("------------------------------------------------------------------------")
    print(f"-             POKEMONES CON FORMA DE {shape}               -")
    print("------------------------------------------------------------------------")
    
    print(tabulate(listaShape, headers="keys", tablefmt='pretty'))

    # listaPokemonsGeneracion=data['pokemon_species']
    # listaPokemonsGeneracion[res.json()['pokemon_species']['name']]=res.json()['pokemon_species']['url']
    # print(listaPokemonsGeneracion)

    # print("------------------------------------------------------------------------")
    # print("- POKEMOS POR GENERACION                                               -")
    # print("------------------------------------------------------------------------")
    # headers = ["Generacion", "Titulo", "Genero"]
    # # print(tabulate(Libro.libros, headers="keys", tablefmt="pretty"))
    #
    # values = [[name, *inner.values()] for name, inner in listaPokemonsGeneracion.items()]
    # print(tabulate(values, headers=headers, tablefmt="pretty"))






