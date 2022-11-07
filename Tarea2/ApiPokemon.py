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


def pokemon_habilidad(id_ability: str) -> None: #Opcion 3
        response = requests.get(url_pokeapi_ability + id_ability)
        data = response.json()
        print("Nombre de la habilidad ingresada:", data["name"])
        lista_pokemons = [pokemons["pokemon"]["name"] for pokemons in data["pokemon"]]
        print("Lista de pokemons:", lista_pokemons)
        for pokemons in lista_pokemons:
            response = requests.get(url_pokeapi + pokemons)
            data = response.json()
            lista_abilities = [habilidades["ability"]["name"] for habilidades in data["abilities"]]
            print("Lista de habilidades:", lista_abilities)
            lista_imagen = data["sprites"]["other"]["official-artwork"]["front_default"]
            print("Url de imagen:" + lista_imagen)



