from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Stats:
    hp: int
    hpperlevel: int
    mp: int
    mpperlevel: int
    movespeed: int
    armor: int
    armorperlevel: float
    spellblock: int
    spellblockperlevel: float
    attackrange: int
    hpregen: float
    hpregenperlevel: float
    mpregen: int
    mpregenperlevel: int
    crit: int
    critperlevel: int
    attackdamage: int
    attackdamageperlevel: float
    attackspeedperlevel: float
    attackspeed: float


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
class SpellStats:
    damage: Optional[List]
    affinity_percent: dict



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
    stats: Optional[SpellStats] = None


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

    def __post_init__(self):
        self.stats = Stats(**self.stats)
