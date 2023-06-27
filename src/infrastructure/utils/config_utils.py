import os
import json

from src.infrastructure.utils.path_utils import PathUtils

root_dir = PathUtils().get_root_path()

config_file_path = os.path.join(root_dir, 'config.json')

with open(config_file_path, 'r') as f:
    config = json.load(f)


class ConfigUtils:

    @classmethod
    def get_config_object(cls, key: str):
        return config[key]
