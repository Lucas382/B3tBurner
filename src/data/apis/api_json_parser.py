import requests
from dataclasses import dataclass, fields
from abc import ABC


@dataclass
class DataClassUnpack(ABC):
    classFieldCache = {}

    @classmethod
    def instantiate(cls, argDict):
        if cls not in cls.classFieldCache:
            cls.classFieldCache[cls] = {f.name for f in fields(cls) if f.init}

        fieldSet = cls.classFieldCache[cls]
        filteredArgDict = {k: v for k, v in argDict.items() if k in fieldSet}
        model = cls(**filteredArgDict)
        return model

    @classmethod
    def get_json(cls, api_url: str):
        response = requests.get(api_url)
        return response.json()
