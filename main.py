import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8c7847577be0ae7ecba6203b5dbb145f'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_registration = {
    "name": "Пачатантра",
    "photo_id": 5
}
body_confirmation = {
    "pokemon_id": "327274",
    "name": " Bri Van de Kamp",
    "photo_id": 25
}

body_pokeball = {
    "pokemon_id": "327274"
}

'''response = requests.post(url = f'{URL}/pokemons',headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_confirmation)
print(response_confirmation.text)
'''
response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_pokeball)
print(response_pokeball.text) 