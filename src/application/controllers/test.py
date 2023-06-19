from src.infrastructure.data.repositories.team_gold_repository import TeamGoldRepository
from src.infrastructure.data.repositories.team_gold_repository2 import TeamGoldRepository2
from src.domain.protocols.team_gold_protocol import TeamGoldProtocol


def print_team_info(team: TeamGoldProtocol) -> None:
    player_name = team.get_player_name()
    team_gold = team.get_team_gold()

    print(f"Player name: {player_name}")
    print(f"Team gold: {team_gold}")


repository = TeamGoldRepository()
repository2 = TeamGoldRepository2()
print_team_info(repository2)

# now = datetime.utcnow()
# rounded_seconds = (now.second // 10) * 10
# rounded_time = now.replace(second=rounded_seconds, microsecond=0)
# iso_timestamp = rounded_time.isoformat() + "Z"
#
# with open('../../../config.json', 'r') as f:
#     config = json.load(f)
# API_HEADERS = config['api_headers']
#
# url = 'https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=pt-BR'
#
#
# def string_to_date(date: str) -> datetime:
#     return datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
#


# response = requests.get(url, headers=API_HEADERS)
#
#
# if response.status_code == 200:
#     data = response.json()
#     with open('result.json', 'w') as file:
#         json.dump(data, file)
#
# else:
#     print('Erro na solicitação:', response.status_code)

# matchs = []
# with open('result.json', 'r') as file:
#     data = json.load(file)
#
# for event in data['data']['schedule']['events']:
#     if event['league']['name'] == 'LPL':
#         match = ScheduleItem(**event)
#         matchs.append(match)
#
# games = []
# for match in matchs:
#     if match.state == 'unstarted':
#         datetime_obj = string_to_date(iso_timestamp)
#         startTime = string_to_date(match.startTime)
#
#         if startTime.date() == datetime_obj.date():
#             print(match.match.teams[0].name, " Vs ", match.match.teams[1].name, " dia ",startTime.date().day, "as", startTime.time().hour)

