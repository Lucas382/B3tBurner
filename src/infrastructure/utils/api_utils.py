# api_utils.py
import requests
from src.infrastructure.utils.config_utils import ConfigUtils

config = ConfigUtils()
API_HEADERS = config.get_config_object('api_headers')
CONFIG_URL = config.get_config_object('external_urls')


def get_api_data(config_url_key: str, config_header_key: str, url_path: str = '', param: str = '') -> dict:
    """
    Retrieves data from an external API.
    :return (dict): The data obtained from the API.
    """
    api_url = CONFIG_URL[config_url_key]
    api_headers = API_HEADERS[config_header_key]

    if param:
        api_url = api_url.format(param=param)
    if url_path:
        api_url += f'/{url_path}'

    response = requests.get(api_url, headers=api_headers)
    if response.status_code == 200:
        return response.json()
    else:
        print('Error in request:', response.status_code)
        return {}
