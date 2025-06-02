import requests
import pytest 


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8c7847577be0ae7ecba6203b5dbb145f'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '33394'
TRAINER_NAME = 'Гатц'


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get (url = f'{URL}/trainers/{TRAINER_ID}')
    assert response_get.json()["trainer_name"] == TRAINER_NAME