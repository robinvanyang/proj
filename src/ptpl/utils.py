import os
from typing import AnyStr


def get_script_path() -> AnyStr:
    script_path = os.path.split(os.path.realpath(__file__))[0]
    return script_path


def get_template_path() -> AnyStr:
    return os.path.join(get_script_path(), "tpl")
