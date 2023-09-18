from fastapi import APIRouter
import requests
import asyncio

from app.models.pokemons import Pokemon
from app.database.database import collection_name
from app.schema.schemas import list_serial, pokemon_serial
from app.db_filler import download_pokemons as download_pokemons_db

router = APIRouter()


@router.get("/")
async def get_pokemons():
    return list_serial(collection_name.find({}))


@router.get("/{pokemon_id}/")
async def get_pokemon_by_id(pokemon_id: int):
    return list_serial(collection_name.find({'id': pokemon_id}))


@router.post("/download_pokemons/")
async def download_pokemons():
    bg_tasks = set()
    task = asyncio.create_task(download_pokemons_db())
    bg_tasks.add(task)
    task.add_done_callback(bg_tasks.discard)
    # asyncio.run(download_pokemons_db())


@router.post("/download_pokemon/{pokemon_id}")
async def download_pokemon_by_id(pokemon_id: int):
    if len(list_serial(collection_name.find({'id': pokemon_id}))) == 0:
        response = requests.get(url=f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}').json()
        collection_name.insert_one(pokemon_serial(dict(Pokemon(**response))))
    else:
        return 'Pokemon is already in collection'


@router.delete('/delete_pokemons/')
async def delete_pokemons():
    collection_name.delete_many({})


@router.delete('/delete_pokemon/{pokemon_id}')
async def delete_pokemon_by_id(pokemon_id: int):
    collection_name.find_one_and_delete({'id': pokemon_id})




