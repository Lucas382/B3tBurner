import re

import requests
from src.domain.models.champion_base_model import ChampionBaseModel
from src.domain.models.champion_model import ChampionModel, Spell, Stats, SpellStats
from src.infrastructure.scraping.champion_scraper import ChampionScraper


class ChampionService:

    @classmethod
    def get_champion_information(cls, champion_name: str, level: int):
        # TODO: Metodo possui ineficiencia para campeões com habilidades especificas como R da karma e R do Sylas.
        # TODO: Alterado classe SpellSts para ter mais attrs, alterar esse metodo para corresponder ao novo modelo.
        """
        Returns a ChampionModel object with information about the champion.
        :param champion_name: The name of the champion.
        :param level: The level of the champion.
        :return: A ChampionModel object.
        """
        spells = {}

        passive = None
        spell_info = ChampionScraper().get_champion_spell_information(champion_name.capitalize())

        for key, value in spell_info.items():
            if value and key != 'passive':
                s_damage = value[0][level - 1]
                s_type = re.search(r'([A-Z]+)', value[1][0]).group()
                s_affinity_percent = {s_type: re.search(r'(\d+)', value[1][0]).group()}
                if len(value) > 2 and len(value[2]) > 0:
                    aditional_type = re.search(r'([A-Z]+)', value[2][0]).group() if re.search(r'([A-Z]+)', value[2][0]) else 'tmp' # TODO: Adicionar um objeto para lidar com os tipos de dano
                    s_affinity_percent[aditional_type] = re.search(r'(\d+)', value[2][0]).group()

                spells[key] = SpellStats(damage=s_damage, affinity_percent=s_affinity_percent)
            else:
                spells[key] = SpellStats(damage=0, affinity_percent={})
                passive = spell_info['passive']
        return passive, spells


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
            champion_spells_url = f"http://ddragon.leagueoflegends.com/cdn/13.3.1/data/en_US/champion/{name}.json"
            spells_damage_url = f"https://raw.communitydragon.org/13.11/game/data/characters/{name.lower()}/{name.lower()}.bin.json"
            champion_data_name = ChampionBaseModel(**requests.get(champion_spells_url).json()).data[name]

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

            champion_instance.stats = Stats(**champion_data_name['stats'])
            champion_instance_list.append(champion_instance)

        return champion_instance_list
