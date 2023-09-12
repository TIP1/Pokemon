from typing import Dict, List
from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    abilities: List[Dict]
    stats: List[Dict]
    moves: List[Dict]

    def __init__(self, **data):
        super().__init__(**data)
        self.abilities = [self.get_ability(ability) for ability in self.abilities]
        self.stats = {stat['stat']['name']: stat['base_stat'] for stat in self.stats}
        self.moves = [self.get_move(move) for move in self.moves]

    def get_ability(self, ability):
        return {'ability_name': ability['ability']["name"], 'ability_url': ability['ability']["url"]}

    def get_move(self, move):
        return {'move_name': move['move']["name"], 'move_url': move['move']["url"]}


        # 'abilities': [
        #     {'abilitiy_name': skill['ability']['name'], 'abilitiy_url': skill['ability']['url']} for skill in pokemon['abilities']
        # ],
        # 'stats': {stat['stat']['name']: stat['base_stat'] for stat in pokemon['stats']},
        # 'moves': [{'move_name': move['move']['name'], 'move_url': move['move']['url']} for move in pokemon['moves']],