from src.domain.models.champion_base_model import ChampionBaseModel
from src.domain.models.live_details_model import LiveDetailsModel, LiveDetailsParticipant
from src.domain.models.live_stats_model import LiveStatusModel


def main():

    api_url = "https://feed.lolesports.com/livestats/v1/window/109625152897792292?hl=pt-BR&startingTime=2023-02-18T10:55:30.000Z"
    live_url = "https://feed.lolesports.com/livestats/v1/details/109539822194338807?hl=pt-BR&startingTime=2023-02-27T17:18:40.000Z"

    live_status = LiveDetailsModel.instantiate(LiveDetailsModel.get_json(live_url))
    participant = LiveDetailsParticipant.instantiate(live_status.frames[0]['participants'][0])

    print(participant.abilities)

    model = LiveStatusModel.instantiate(LiveDetailsModel.get_json(api_url))
    names = model.get_champions_red_team

    chamdata = ChampionBaseModel.instantiate(ChampionBaseModel.get_json("http://ddragon.leagueoflegends.com/cdn/13.3.1/data/en_US/champion.json"))

    for champ in model.get_champion_information_list(names):
        # print(f"{champ.id} tem {champ.stats.attackdamage} de atk")
        print(f"O Q effect de {champ.id} é {champ.spell_r.effect[1]}")


if __name__ == "__main__":
    main()
