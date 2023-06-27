import os

current_dir = os.path.abspath(os.path.dirname(__file__))
root_dir = None
while root_dir is None or root_dir == current_dir:
    if os.path.isfile(os.path.join(current_dir, 'config.json')):
        root_dir = current_dir
    current_dir = os.path.abspath(os.path.join(current_dir, os.pardir))


if root_dir is None:
    raise ValueError("Root directory not found")


class PathUtils:

    @classmethod
    def get_root_path(cls):
        return root_dir
