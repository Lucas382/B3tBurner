from dataclasses import dataclass
from typing import List

@dataclass
class PerkMetadata:
    styleId: int
    subStyleId: int
    perks: List[int]

@dataclass
class LiveDetailsParticipantModel:
    participantId: str
    level: str
    kills: str
    deaths: str
    assists: str
    totalGoldEarned: str
    creepScore: str
    killParticipation: str
    championDamageShare: str
    wardsPlaced: str
    wardsDestroyed: str
    attackDamage: str
    abilityPower: str
    criticalChance: str
    attackSpeed: str
    lifeSteal: str
    armor: str
    magicResistance: str
    tenacity: str
    items: List[str]
    perkMetadata: PerkMetadata
    abilities: List[str]

    def __post_init__(self):
        self.perkMetadata = PerkMetadata(**self.perkMetadata)


@dataclass
class LiveDetailsModel:
    frames: dict

