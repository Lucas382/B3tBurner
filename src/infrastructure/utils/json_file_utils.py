import os
import json

from src.infrastructure.utils.path_utils import PathUtils

root_dir = PathUtils().get_root_path()

FILE_PATH = os.path.join(root_dir, 'src', 'infrastructure', 'data', 'json_data', '{folder}', '{file_name}.json')


def is_file_exists(folder: str, file_name: str) -> bool:
    """
    Checks if a file exists at the specified path.
    :return (bool): True if the file exists, False otherwise.
    """
    file_path = FILE_PATH.format(folder=folder, file_name=file_name)
    return os.path.isfile(file_path)


def save_file_data(data: dict, folder: str, file_name: str) -> None:
    """
    Saves the data into a file.
    :param (dict) data: The data to be saved.
    :param (str) folder: The folder name.
    :param (str) file_name: The file name.
    """
    file_path = FILE_PATH.format(folder=folder, file_name=file_name)
    with open(file_path, 'w') as file:
        json.dump(data, file)
        file.write('\n')


def get_file_data(folder: str, file_name: str) -> dict:
    file_path = FILE_PATH.format(folder=folder, file_name=file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
