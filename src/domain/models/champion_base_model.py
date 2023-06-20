from dataclasses import dataclass


@dataclass
class ChampionBaseModel:
    type: str
    format: str
    version: str
    data: str
