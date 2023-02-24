from src.domain.interfaces.team_gold_interface import TeamGoldInterface


class TeamGoldRepository2(TeamGoldInterface):

    def get_player_name(self):
        player_name: str = "Carlos"
        return player_name

    def get_team_gold(self):
        team_gold = 223
        return team_gold
