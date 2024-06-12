import os
from typing import AnyStr


def get_current_folder_name() -> AnyStr:
    path = os.getcwd()
    return os.path.basename(path)
