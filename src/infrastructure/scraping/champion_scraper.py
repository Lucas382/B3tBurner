import requests
import re
from src.infrastructure.utils.config_utils import ConfigUtils

from bs4 import BeautifulSoup

config = ConfigUtils()
CONFIG_HEADERS = config.get_config_object('api_headers')
CONFIG_URL = config.get_config_object('external_urls')


def extract_magic_damage_data(tables):
    """
    Extracts the magic damage data from the given spans.
    :param tables: The spans containing the damage data.
    :return: The extracted magic damage data.
    """
    dmg_element = []
    dmg_keys = ["Magic Damage", "Physical Damage", "True Damage", "Raw Damage", "Damage per Second"]
    for table in tables:
        dt_element = table.find('dt')
        b_element = dt_element.find('b').text

        dd_element = table.find('dd')
        if any(dmg_elem in b_element for dmg_elem in dmg_keys):
            if dd_element:
                text = dd_element.text
                split_text = re.split(r'[/(+]', text)
                dmg_element.extend(split_text)
    return dmg_element


def organize_damage_data(dmg_element):
    """
    Organizes the damage data into a structured list.
    :param dmg_element: The damage data to be organized.
    :return: The organized damage data.
    """
    result = []
    temp = []

    for elem in dmg_element:
        if elem == '':
            if temp:
                result.append(temp)
                temp = []
        else:
            temp.append(elem)

    if temp:
        result.append(temp)

    return result


class ChampionScraper:

    @classmethod
    def get_champion_spell_information(cls, champion_name: str):
        """
        Returns a ChampionModel object with information about the champion.
        :param champion_name: The name of the champion.
        :return: A ChampionModel object.
        """
        html = cls.get_html_content(champion_name)
        spell_info = {
                      'passive': cls.find_champion_passive(html),
                      'q': cls.find_champion_spell(html, 'skill_q'),
                      'w': cls.find_champion_spell(html, 'skill_w'),
                      'e': cls.find_champion_spell(html, 'skill_e'),
                      'r': cls.find_champion_spell(html, 'skill_r')}
        
        return spell_info

    @staticmethod
    def find_champion_passive(html_content: str):
        """
        Returns the passive of the champion.
        :param html_content: The HTML content of the champion page.
        :return: The passive of the champion.
        """
        html = BeautifulSoup(html_content, 'html.parser')
        div_passive = html.find('div', {'class': 'skill_innate'})
        tables = div_passive.find_all('table')
        if tables:
            dmg_element = extract_magic_damage_data(tables)

            if dmg_element:
                return organize_damage_data(dmg_element)
        text = div_passive.getText().replace("\n", "")
        return text

    @staticmethod
    def find_champion_spell(html_content: str, spell_html_class: str):
        """
        Returns the passive of the champion.
        :param html_content: The HTML content of the champion page.
        :return: The passive of the champion.
        """
        html = BeautifulSoup(html_content, 'html.parser')
        div_spell = html.find('div', {'class': spell_html_class})
        tables = div_spell.find_all('table')
        dmg_element = extract_magic_damage_data(tables)

        if dmg_element:
            return organize_damage_data(dmg_element)

        return None


    @staticmethod
    def get_html_content(champion_name: str):
        """
        Returns the HTML content of the champion page.
        :param champion_name: The name of the champion.
        :return: The HTML content of the champion page.
        """

        headers = CONFIG_HEADERS['fandom_header']
        champion_page_url = CONFIG_URL['champion_page_url'].format(champion_name=champion_name)

        # Send a GET request to the URL
        response = requests.get(champion_page_url, headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Access the HTML content
            html_content = response.text
            return html_content
        else:
            print("Failed to retrieve HTML content. Status code:", response.status_code)