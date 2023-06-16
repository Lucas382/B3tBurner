from dataclasses import dataclass
from typing import List
from src.data.apis.api_json_parser import DataClassUnpack


@dataclass
class Record(DataClassUnpack):
    wins: int
    losses: int


@dataclass
class Team(DataClassUnpack):
    name: str
    code: str
    image: str
    result: dict
    record: Record

    def __post_init__(self):
        self.record = Record(**self.record)


@dataclass
class League(DataClassUnpack):
    name: str
    slug: str


@dataclass
class Strategy(DataClassUnpack):
    type: str
    count: int


@dataclass
class Match(DataClassUnpack):
    id: str
    flags: List[str]
    teams: List[Team]
    strategy: Strategy
    def __post_init__(self):
        self.strategy = Strategy(**self.strategy)
        self.teams = [Team(**team) for team in self.teams]


@dataclass
class ScheduleItem(DataClassUnpack):
    startTime: str
    state: str
    type: str
    blockName: str
    league: League
    match: Match

    def __post_init__(self):
        self.league = League(**self.league)
        self.match = Match(**self.match)
