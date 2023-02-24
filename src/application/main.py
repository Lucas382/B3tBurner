from src.data.repositories.team_gold_repository import TeamGoldRepository
from src.data.repositories.team_gold_repository2 import TeamGoldRepository2

from src.services.team_gold_service import GoldDealer
from src.domain.models.team_gold_model import TeamGold


def main():
    repo = TeamGoldRepository() #Repositório que quero usar
    repo2 = TeamGoldRepository2() #Repositório que quero usar
    service = GoldDealer(repo) #Serviço que usa o repositório
    model = TeamGold() #Model a ser preenchida pelos dados

    model.player_1_name = service.return_player_name()
    model.player1 = service.return_team_gold()
    print(model)
    print(model.player_1_name)


if __name__ == "__main__":
    main()
