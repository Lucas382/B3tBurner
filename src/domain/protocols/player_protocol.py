from typing import Protocol


class PlayerServiceProtocol(Protocol):

    def get_players_model_by_name(self, player_name: str):
        ...
