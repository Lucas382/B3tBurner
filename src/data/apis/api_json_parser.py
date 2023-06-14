import requests
from dataclasses import dataclass, fields
from abc import ABC


@dataclass
class DataClassUnpack(ABC):
    """
    A base class for dataclasses with utility methods for instantiation and retrieving JSON data.

    Subclasses of DataClassUnpack can use the `instantiate` method to create an instance of the class
    with values from a dictionary. The dictionary is filtered to include only fields that are defined
    as `init=True` in the dataclass.

    The `get_json` method can be used to make an HTTP GET request to an API endpoint and retrieve the
    response data as a JSON object.

    Note: Subclasses should be decorated with the `@dataclass` decorator to enable dataclass behavior.
    """

    classFieldCache = {}

    @classmethod
    def instantiate(cls, argDict):
        """
        Create an instance of the dataclass with values from a dictionary.

        Only fields that are defined as `init=True` in the dataclass will be included.

        :param argDict: A dictionary containing values for the dataclass fields.
        :return: An instance of the dataclass.
        """
        if cls not in cls.classFieldCache:
            cls.classFieldCache[cls] = {f.name for f in fields(cls) if f.init}

        fieldSet = cls.classFieldCache[cls]
        filteredArgDict = {k: v for k, v in argDict.items() if k in fieldSet}
        model = cls(**filteredArgDict)
        return model

    @classmethod
    def get_json(cls, api_url: str):
        """
       Make an HTTP GET request to an API endpoint and retrieve the response data as a JSON object.

       :param api_url: The URL of the API endpoint.
       :return: A JSON object representing the response data.
       """
        response = requests.get(api_url)
        return response.json()
