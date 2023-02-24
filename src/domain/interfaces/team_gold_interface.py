from abc import ABC, abstractmethod


class TeamGoldInterface(ABC):

    @abstractmethod
    def get_player_name(self):
        pass

    @abstractmethod
    def get_team_gold(self):
        pass
