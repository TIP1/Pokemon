import asyncio
import pytest

from app.routers.route import download_pokemon_by_id, get_pokemons, get_pokemon_by_id,\
    delete_pokemons, delete_pokemon_by_id
from app.db_filler import download_pokemons
from fixtures import clean_db

class TestApi:
    @pytest.mark.asyncio
    async def test_download_pokemons(self, clean_db):
        await download_pokemons()
        pokemons = await get_pokemons()
        assert len(pokemons) == 151, 'Database filler method doesn\'t work correct!'

    def test_get_pokemon_by_id(self):
        try:
            pokemon = asyncio.run(get_pokemon_by_id(1))[0]
        except IndexError:
            raise ValueError('Pokemon is not in collection')
        assert pokemon['id'] == 1, 'Wrong pokemon was got!'

    def test_delete_pokemon_by_id(self):
        asyncio.run(delete_pokemon_by_id(1))
        pokemon = asyncio.run(get_pokemon_by_id(1))
        assert len(pokemon) == 0, 'Something went wrong during delete proccess!'

    def test_download_pokemon_by_id(self):
        asyncio.run(download_pokemon_by_id(1))
        pokemon = asyncio.run(get_pokemon_by_id(1))
        assert len(pokemon) == 1, 'Something went wrong during download proccess!'

    def test_delete_pokemons(self):
        pokemons_len = len(asyncio.run(get_pokemons()))
        asyncio.run(delete_pokemons())
        pokemons_len_new = len(asyncio.run(get_pokemons()))
        assert pokemons_len_new == 0 and pokemons_len != pokemons_len_new


