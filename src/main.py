import re

from src.domain.models.champion_model import SpellStats
from src.domain.protocols.champion_protocol import ChampionServiceProtocol
from src.domain.models.live_details_model import LiveDetailsModel, LiveDetailsParticipantModel
from src.domain.models.live_stats_model import LiveStatusModel
from src.domain.protocols.live_details_protocol import LiveDetailsServiceProtocol
from src.domain.services.champion_service import ChampionService
from src.domain.protocols.player_protocol import PlayerServiceProtocol
import requests

from src.domain.services.live_details_service import LiveDetailsService
from src.domain.services.player_service import PlayerDataService


def main():

    api_url = "https://feed.lolesports.com/livestats/v1/window/109625152897792292?hl=pt-BR&startingTime=2023-02-18T10:55:30.000Z"
    live_url = "https://feed.lolesports.com/livestats/v1/details/109539822194338807?hl=pt-BR&startingTime=2023-02-27T17:18:40.000Z"

    live_games_url = "https://esports-api.lolesports.com/persisted/gw/getLive?hl=pt-BR"
    schedule_games_lpl_url = "https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=pt-BR"

    live_status = LiveDetailsModel(**requests.get(live_url).json())

    level = live_status.frames[-1]['participants'][0]['abilities'].count('R')
    # print(details)

    model = LiveStatusModel(**requests.get(api_url).json())
    names = model.get_champions_red_team

    champion_service_protocol: ChampionServiceProtocol = ChampionService()

    champs = champion_service_protocol.get_champion_information_list(names)
    # print(champs)
    for champ in champs:
        print(champ.name)
        p, spells = champion_service_protocol.get_champion_information(champ.name, level)
        champ.spell_q.stats = spells['q']
        champ.spell_w.stats = spells['w']
        champ.spell_e.stats = spells['e']
        champ.spell_r.stats = spells['r']

        print(champ.spell_q.stats.affinity_percent, champ.spell_w.stats.affinity_percent, champ.spell_e.stats.affinity_percent,  champ.spell_r.stats.affinity_percent)
        # print(f"{champ.name} Q tem: {champ.spell_q.stats.damage} + {champ.spell_q.stats.affinity_percent['AP']} de dano")

    # for name in names:

    # live_details_service_protocol: LiveDetailsServiceProtocol = LiveDetailsService()
    # details = live_details_service_protocol.get_today_matches_by_league('lpl')
    # player_service_protocol: PlayerServiceProtocol = PlayerDataService()
    #
    # faker = player_service_protocol.get_players_model_by_name('chovy')

    # print(details)
    # print(faker)

    # champion_info_list = champion_service_protocol.get_champion_information_list(names)
    #
    # for champ in champion_info_list:
    #     print(f"O dano de {champ.id} é {champ.stats.attackdamage}")


if __name__ == "__main__":
    main()
