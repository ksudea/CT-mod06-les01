import requests
from bs4 import BeautifulSoup
import json

# Task 2

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text
pikachu_data = json.loads(json_data)

print(pikachu_data["name"])
print(pikachu_data["abilities"])

# Task 3

def fetch_pokemon_data(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
    response = requests.get(url)
    json_data = response.text
    pokemon_data = json.loads(json_data)
    print(pokemon_data['name'])
    print(pokemon_data['abilities'])
    return pokemon_data

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for name in pokemon_list:
        pokemon_weight = fetch_pokemon_data(name)['weight']
        total_weight += pokemon_weight
    print(total_weight / len(pokemon_list))

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
calculate_average_weight(pokemon_names)
