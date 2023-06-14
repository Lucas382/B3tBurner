import json
from dataclasses import dataclass, field
from src.data.apis.api_json_parser import DataClassUnpack


@dataclass
class ChampionBaseModel(DataClassUnpack):
    type: str
    format: str
    version: str
    data: str
