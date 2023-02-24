from src.domain.interfaces.team_gold_interface import TeamGoldInterface


class GoldDealer:

    def __init__(self, repo: TeamGoldInterface) -> None:
        self.__repo = repo

    def return_team_gold(self):
        gold = self.__repo.get_team_gold()
        return gold

    def return_player_name(self):
        name = self.__repo.get_player_name()
        return name
