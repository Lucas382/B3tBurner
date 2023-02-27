from dataclasses import dataclass
from typing import Type

from src.data.apis.api_json_parser import DataClassUnpack
from src.domain.models.champion_base_model import ChampionBaseModel
from src.domain.models.champion_model import ChampionModel, Stats


def teste():
    print("teste")
@dataclass()
class LiveStatusModel(DataClassUnpack):

    esportsGameId: str
    esportsMatchId: str
    gameMetadata: str
    frames: str

    @property
    def get_champions_blue_team(self):
        champ_list = []
        for champ in self.gameMetadata['blueTeamMetadata']['participantMetadata']:
            champ_list.append(champ['championId'])
        return champ_list

    @property
    def get_champions_red_team(self):
        champ_list = []
        for champ in self.gameMetadata['redTeamMetadata']['participantMetadata']:
            champ_list.append(champ['championId'])
        return champ_list

    @classmethod
    def get_champion_information_list(cls, champions_names):
        champion_spells_list = []
        for name in champions_names:
            champion_instance = ChampionModel()
            champion_spells_url = f"http://ddragon.leagueoflegends.com/cdn/13.3.1/data/en_US/champion/{name}.json"
            champion_data_name = ChampionBaseModel.instantiate(ChampionBaseModel.get_json(champion_spells_url)).data[name]
            champion_instance.id = champion_data_name['id']
            champion_instance.name = champion_data_name['name']
            champion_instance.passive = champion_data_name['passive']
            champion_instance.spell_q = champion_data_name['spells'][0]
            champion_instance.spell_w = champion_data_name['spells'][1]
            champion_instance.spell_e = champion_data_name['spells'][2]
            champion_instance.spell_r = champion_data_name['spells'][3]

            atk = champion_data_name['stats']['attackdamage']
            armor = champion_data_name['stats']['armor']
            spellblock = champion_data_name['stats']['spellblock']

            champion_instance.stats = Stats(atk, armor, spellblock)

            champion_spells_list.append(champion_instance)

        return champion_spells_list
