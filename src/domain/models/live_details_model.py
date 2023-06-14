from dataclasses import dataclass, field
from src.data.apis.api_json_parser import DataClassUnpack


@dataclass
class LiveDetailsParticipant(DataClassUnpack):
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
    items: list[str]
    abilities: list[str]


@dataclass
class LiveDetailsModel(DataClassUnpack):
    frames: str

