from dataclasses import dataclass, field

@dataclass
class Stats:
    attackdamage: str
    armor: str
    spellblock: str

@dataclass
class ChampionModel:
    id: str = field(init=False)
    name: str = field(init=False)
    passive: str = field(init=False)
    spell_q: str = field(init=False)
    spell_w: str = field(init=False)
    spell_e: str = field(init=False)
    spell_r: str = field(init=False)
    stats: Stats = field(init=False)


