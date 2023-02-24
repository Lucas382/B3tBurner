from src.domain.interfaces.team_gold_interface import TeamGoldInterface


class TeamGoldRepository(TeamGoldInterface):

    def get_player_name(self):
        player_name: str = "Julio"
        return player_name

    def get_team_gold(self):
        team_gold = 3129
        return team_gold
