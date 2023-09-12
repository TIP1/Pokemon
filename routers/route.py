from fastapi import APIRouter
from models.pokemons import Pokemon
from database.database import collection_name, db
from schema.schemas import list_serial, pokemon_serial
import requests
from bson import ObjectId

router = APIRouter()


@router.get("/pokemon/all/") #/pokemons/
async def get_pokemons():
    return list_serial(collection_name.find({}))


@router.get("/pokemon/{pokemon_id}/") #/pokemons/{id}
async def get_pokemon(pokemon_id: int):
    return list_serial(collection_name.find({'id': pokemon_id}))


@router.post("/download_pokemons/all")
async def download_pokemons():
    pokemons = []
    for index in range(151):
        response = requests.get(url=f'https://pokeapi.co/api/v2/pokemon/{index+1}').json()
        pokemons.append(dict(Pokemon(**response)))
    collection_name.insert_many(list_serial(pokemons))


@router.post("/download_pokemons/{pokemon_id}")
async def download_pokemons(pokemon_id: int):
    response = requests.get(url=f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}').json()
    collection_name.insert_one(pokemon_serial(dict(Pokemon(**response))))


@router.delete('/delete_pokemon/all')
async def delete_pokemon():
    collection_name.delete_many({})


@router.delete('/delete_pokemon/{pokemon_id}')
async def delete_pokemon(pokemon_id: int):
    collection_name.find_one_and_delete({'id': pokemon_id})




