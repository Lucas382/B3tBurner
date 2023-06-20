import json
import os
import requests

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(f'../../config.json', 'r') as f:
    config = json.load(f)

API_HEADERS = config['api_headers']
MATCH_SCHEDULE_URL = config['external_urls']['match_schedule_url']

FILE_PATH = os.path.join(CURRENT_DIR, '../', 'data', 'json_data', 'games', 'matchSchedule.json')


def get_match_schedule_data() -> dict:
    """
    Retrieves the match schedule data either from the local file or from the external API if the file is not found.
    :return (dict) : The match schedule data.
    """
    match_schedule_data = {}

    if not os.path.isfile(FILE_PATH):
        response = requests.get(MATCH_SCHEDULE_URL, headers=API_HEADERS)
        if response.status_code == 200:
            match_schedule_data = response.json()
            save_match_schedule_data(match_schedule_data)
        else:
            print('Erro na solicitação:', response.status_code)
    else:
        with open(FILE_PATH, 'r') as file:
            match_schedule_data = json.load(file)

    return match_schedule_data


def save_match_schedule_data(match_schedule_data: dict):
    """
    Saves the match schedule data to the local file.
    :param match_schedule_data : The match schedule data to be saved.
    :return:
    """
    with open(FILE_PATH, 'w') as file:
        json.dump(match_schedule_data, file)


def save_match_json(match_json: str):
    """
    Saves the match JSON to the local file.
    :param match_json : The match JSON to be saved.
    :return:
    """
    with open(FILE_PATH, 'w') as file:
        json.dump(match_json, file)
