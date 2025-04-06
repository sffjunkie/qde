from pathlib import Path
from typing import Any

from libqtile.log_utils import logger  # type: ignore

from ..fs import read_yaml, user_config_dir
from .model import Settings
from .default import DEFAULT_SETTINGS


def _settings_path(filepath: Path | None = None) -> Path | None:
    settings_path: Path | None
    if filepath is not None and filepath.is_absolute():
        settings_path = filepath
    else:
        if filepath is None:
            filepath = Path("settings.yaml")

        settings_path = user_config_dir() / filepath

    if settings_path is not None and not settings_path.exists():
        logger.warning(f"No settings found in {settings_path}")
        settings_path = None

    return settings_path


def _dict_to_settings(data: dict[str, Any]) -> Settings:
    settings = Settings.model_validate(data)
    return settings


def load_settings(filepath: Path | None = None) -> Settings:
    settings_path = _settings_path(filepath)
    data = read_yaml(settings_path)
    if data is None:
        settings_data = {}
    else:
        settings_data = DEFAULT_SETTINGS | data | {"path": settings_path}
    return _dict_to_settings(settings_data)
