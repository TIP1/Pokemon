from models.pokemons import Pokemon
from typing import List

def pokemon_serial(pokemon: dict) -> dict:
    return {
        'id': pokemon['id'],
        'name': pokemon['name'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'abilities': pokemon['abilities'],
        'stats': pokemon['stats'],
        'moves': pokemon['moves'],
    }

def list_serial(pokemons: List[dict]) -> List[dict]:
    return [pokemon_serial(pokemon) for pokemon in pokemons]

# def pokemon_serial(pokemon: Pokemon) -> dict:
#     return {
#         'id': pokemon.id,
#         'name': pokemon.name,
#         'height': pokemon.height,
#         'weight': pokemon.weight,
#         'abilities': pokemon.abilities,
#         'stats': pokemon.stats,
#         'moves': pokemon.moves,
#     }


# def list_serial(pokemons: List[Pokemon]) -> List[dict]:
#     return [pokemon_serial(pokemon) for pokemon in pokemons]
