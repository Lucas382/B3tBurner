from dataclasses import dataclass


@dataclass
class TeamGold:
    player_1_name: str = ""
    player1: int = 0
    player2: int = 0
    player3: int = 0
    player4: int = 0
    player5: int = 0

    def get_all_players(self):
        return [self.player1, self.player2, self.player3, self.player4, self.player5]

