from dataclasses import dataclass
from typing import List


@dataclass
class Stats:
    attackdamage: str
    armor: str
    spellblock: str


@dataclass
class LevelTip:
    label: List[str]
    effect: List[str]


@dataclass
class Image:
    full: str
    sprite: str
    group: str
    x: int
    y: int
    w: int
    h: int


@dataclass
class Spell:
    id: str
    name: str
    description: str
    tooltip: str
    leveltip: LevelTip
    maxrank: int
    cooldown: List[int]
    cooldownBurn: str
    cost: List[int]
    costBurn: str
    datavalues: dict
    effect: List[any]
    effectBurn: List[str]
    vars: List[any]
    costType: str
    maxammo: str
    range: List[int]
    rangeBurn: str
    image: Image
    resource: str


@dataclass(init=False)
class ChampionModel:
    id: str
    name: str
    passive: str
    spell_q: Spell
    spell_w: Spell
    spell_e: Spell
    spell_r: Spell
    stats: Stats

