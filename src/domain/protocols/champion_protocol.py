from typing import List, Protocol
from src.domain.models.champion_model import ChampionModel

#a interface for champion_service


class ChampionServiceProtocol(Protocol):
    def get_champion_information_list(self, champions_names: List[str]) -> List[ChampionModel]:
        ...
