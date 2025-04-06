from pathlib import Path
from typing import Any

from libqtile.log_utils import logger  # type: ignore

from ...fs import read_yaml, user_config_dir
from .model import Keyboard, Pointer, InputConfiguration


def _input_path(filepath: Path | None = None) -> Path | None:
    settings_path: Path | None
    if filepath is not None and filepath.is_absolute():
        settings_path = filepath
    else:
        if filepath is None:
            filepath = Path("input.yaml")

        settings_path = user_config_dir() / filepath

    if settings_path is not None and not settings_path.exists():
        logger.warning(f"No input configuration found in {settings_path}")
        settings_path = None

    return settings_path


def _dict_to_input_configuration(data: dict[str, Any]) -> InputConfiguration:
    keyboards = {}
    for name, props in data["keyboard"].items():
        kb = Keyboard.model_validate(props)
        keyboards[name] = kb

    pointers = {}
    for name, props in data["pointer"].items():
        pointer = Pointer.model_validate(props)
        pointers[name] = pointer

    return InputConfiguration(keyboard=keyboards, pointer=pointers)


def load_inputs(filepath: Path | None = None) -> InputConfiguration:
    input_path = _input_path(filepath)
    data = read_yaml(input_path)
    if data is None:
        input_data = {}
    else:
        input_data = data | {"path": input_path}
    return _dict_to_input_configuration(input_data)
