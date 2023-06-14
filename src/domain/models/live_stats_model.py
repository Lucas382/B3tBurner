from dataclasses import dataclass
from src.data.apis.api_json_parser import DataClassUnpack
from src.domain.models.champion_base_model import ChampionBaseModel
from src.domain.models.champion_model import ChampionModel, Spell
import requests

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
        """
        Returns a list with the champions id of the blue team.
        :return: list of champions id.
        """
        champ_list = []
        for champ in self.gameMetadata['blueTeamMetadata']['participantMetadata']:
            champ_list.append(champ['championId'])
        return champ_list

    @property
    def get_champions_red_team(self):
        """
        Returns a list with the champions id of the red team.
        :return: list of champions id.
        """
        champ_list = []
        for champ in self.gameMetadata['redTeamMetadata']['participantMetadata']:
            champ_list.append(champ['championId'])
        return champ_list

    @classmethod
    def get_champion_information_list(cls, champions_names):
        """
        Returns a list of ChampionModel objects with information about each champion.
        :param champions_names: A list of champion names.
        :return: A list of ChampionModel objects.
        """
        champion_instance_list = []
        for name in champions_names:
            champion_instance = ChampionModel()
            champion_spells_url = f"http://ddragon.leagueoflegends.com/cdn/13.3.1/data/en_US/champion/{name}.json" #TODO: chage version to actual version
            spells_damage_url = f"https://raw.communitydragon.org/13.11/game/data/characters/{name.lower()}/{name.lower()}.bin.json" #TODO: chage version to actual version
            champion_data_name = ChampionBaseModel.instantiate(ChampionBaseModel.get_json(champion_spells_url)).data[name]

            response = requests.get(spells_damage_url)
            data = response.json()


            champion_instance.id = champion_data_name['id']
            champion_instance.name = champion_data_name['name']
            champion_instance.passive = champion_data_name['passive']

            champion_instance.spell_q = Spell(**champion_data_name['spells'][0])
            champion_instance.spell_w = Spell(**champion_data_name['spells'][1])
            champion_instance.spell_e = Spell(**champion_data_name['spells'][2])
            champion_instance.spell_r = Spell(**champion_data_name['spells'][3])

            if champion_instance.spell_q.effect[1][0] == 0:
                champion_instance.spell_q.effect[1] = data[f"Characters/{name}/Spells/{champion_instance.spell_q.id}Ability/{champion_instance.spell_q.id}"]["mSpell"]["mDataValues"][0]["mValues"]

            if champion_instance.spell_w.effect[1][0] == 0:
                champion_instance.spell_w.effect[1] = data[f"Characters/{name}/Spells/{champion_instance.spell_w.id}Ability/{champion_instance.spell_w.id}"]["mSpell"]["mDataValues"][0]["mValues"]

            if champion_instance.spell_e.effect[1][0] == 0:
                champion_instance.spell_e.effect[1] = data[f"Characters/{name}/Spells/{champion_instance.spell_e.id}Ability/{champion_instance.spell_e.id}"]["mSpell"]["mDataValues"][0]["mValues"]

            if champion_instance.spell_r.effect[1][0] == 0:
                try:
                    champion_instance.spell_r.effect[1] = data[f"Characters/{name}/Spells/{champion_instance.spell_r.id}Ability/{champion_instance.spell_r.id}"]["mSpell"]["mDataValues"][0]["mValues"]
                except:
                    pass

            champion_instance_list.append(champion_instance)

        return champion_instance_list
