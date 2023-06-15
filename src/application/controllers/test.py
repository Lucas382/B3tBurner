import json
import requests
from src.domain.models.match_schedule_model import ScheduleItem


with open('../../../config.json', 'r') as f:
    config = json.load(f)

api_key = config['api_key']

url = 'https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=pt-BR'
headers = {
    'authority': 'esports-api.lolesports.com',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'origin': 'empty',
    'pragma': 'no-cache',
    'referer': 'empty',
    'sec-ch-ua': '"Chromium";v="112", "Not_A Brand";v="24", "Opera GX";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0',
    'x-api-key': api_key

}

# response = requests.get(url, headers=headers)
#
#
# if response.status_code == 200:
#     data = response.json()
#     with open('result.json', 'w') as file:
#         json.dump(data, file)
#
# else:
#     print('Erro na solicitação:', response.status_code)

matchs = []
with open('result.json', 'r') as file:
    data = json.load(file)
    for event in data['data']['schedule']['events']:
        if event['league']['name'] == 'LPL':
            match = ScheduleItem(**event)
            matchs.append(match)

games = []
for match in matchs:
    if match.state == 'unstarted':
        print(match.match.teams[0].record)

