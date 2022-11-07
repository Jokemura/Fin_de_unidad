import json

import requests
from tabulate import tabulate

listaPokemonsGeneracion={}

@staticmethod
def listarGeneraciion():
    url = "https://pokeapi.co/api/v2/generation/"
    idGeneracion=input("Ingresa la generacion: ")
    res = requests.get(url+idGeneracion)
    data=res.json()
    json_object = json.loads(data)

    # listaPokemonsGeneracion=data['pokemon_species']
    # listaPokemonsGeneracion[res.json()['pokemon_species']['name']]=res.json()['pokemon_species']['url']
    # print(listaPokemonsGeneracion)
    print(json_object['id'])
    # print("------------------------------------------------------------------------")
    # print("- POKEMOS POR GENERACION                                               -")
    # print("------------------------------------------------------------------------")
    # headers = ["Generacion", "Titulo", "Genero"]
    # # print(tabulate(Libro.libros, headers="keys", tablefmt="pretty"))
    #
    # values = [[name, *inner.values()] for name, inner in listaPokemonsGeneracion.items()]
    # print(tabulate(values, headers=headers, tablefmt="pretty"))