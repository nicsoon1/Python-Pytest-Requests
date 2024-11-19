import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOK = '3c15fc3c57ae26f7c377d504c69fd1b8'
HEADER = {'Content-Type' : 'application/json', "trainer_token" : TOK}
trainer_id = '11722'

def test_status_code():
    response = requests.get(f'{URL}/v2/trainers', params = {'trainer_id' : trainer_id})
    assert response.status_code == 200 
def test_trainer_name():
    response_name = requests.get(f'{URL}/v2/trainers', params = {'trainer_id' : trainer_id})
    assert response_name.json()["data"][0]["trainer_name"] == "Gena"    