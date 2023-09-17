import json
import aiohttp
import asyncio

from app.database.database import collection_name
from app.schema.schemas import list_serial
from app.models.pokemons import Pokemon


async def fetch(s, index):
    async with s.get(url=f'https://pokeapi.co/api/v2/pokemon/{index}') as resp:
        return await resp.text()


async def fetch_all(s, indexes):
    tasks = []
    for index in range(1, indexes):
        task = asyncio.create_task(fetch(s, index))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res


async def download_pokemons():
    if len(list_serial(collection_name.find({}))) == 0:
        async with aiohttp.ClientSession() as session:
            downloaded_pokemons = await fetch_all(session, 152)
            pokemons = []
            for pokemon in downloaded_pokemons:
                try:
                    # if len(list_serial(collection_name.find({'id': pokemon['id']}))) == 0:
                    pokemons.append(dict(Pokemon(**(json.loads(pokemon)))))
                except:
                    continue
            collection_name.insert_many(list_serial(pokemons))
