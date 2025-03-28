import configparser
import os
import random
import string
from itertools import chain
from pathlib import Path
from typing import Any

import yaml

CONFIG_DIR = "qde"


def user_config_dir(config_dir: str = CONFIG_DIR) -> Path:
    xdg_config = Path(
        os.environ.get(
            "XDG_CONFIG_HOME",
            os.path.expanduser("~/.config"),
        )
    )
    return xdg_config / config_dir


def read_yaml(filepath: Path | None = None) -> dict[str, Any]:
    data = {}
    if filepath is not None:
        try:
            with open(filepath, "r") as fp:
                data = yaml.load(fp, yaml.SafeLoader)
        except (IOError, yaml.YAMLError):
            pass

    return data


class _MultiDict(dict):
    def __setitem__(self, key, value):
        if isinstance(value, list) and key in self:
            self[key].extend(value)
        else:
            super().__setitem__(key, value)


def read_ini(filepath: Path, has_sections: bool = True) -> dict[str, str]:
    data = {}
    parser = configparser.ConfigParser(
        strict=False,
        empty_lines_in_values=False,
        dict_type=_MultiDict,
        interpolation=None,
    )
    dummy = "".join(random.choices(string.ascii_uppercase + string.digits, k=16))
    try:
        with open(filepath, "r") as fp:
            lines = fp.readlines()

            if not has_sections:
                contents = chain((f"[{dummy}]\n",), lines)
            else:
                contents = lines

            parser.read_file(contents)

            items = parser.items(dummy)
            for name, value in items:
                if "\n" in value:
                    data[name] = value.split("\n")
                else:
                    data[name] = value
    except IOError:
        pass

    return data
