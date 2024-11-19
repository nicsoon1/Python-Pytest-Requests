import requests

URL = 'https://api.pokemonbattle.ru'
TOK = '3c15fc3c57ae26f7c377d504c69fd1b8'
HEADER = {'Content-Type' : 'application/json', "trainer_token" : TOK}
body = {
    "name": "gena",
    "photo_id": 33
}

response = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body)
print(response.text)

pokemon_id = response.json()['id']
print(pokemon_id)

response_name = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = {"pokemon_id": pokemon_id,
    "name": "NewBI",
    "photo_id": 33
})
print(response_name.text)

response_pok = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = {
    "pokemon_id": pokemon_id
})
print(response_pok.text)