from pathlib import Path
from typing import Any

from libqtile.log_utils import logger  # type: ignore

from ...fs import read_yaml, user_config_dir
from .model import GroupConfiguration
from .default import DEFAULT_GROUPS


def _group_path(filepath: Path | None = None) -> Path | None:
    group_path: Path | None
    if filepath is not None and filepath.is_absolute():
        group_path = filepath
    else:
        if filepath is None:
            filepath = Path("group.yaml")

        group_path = user_config_dir() / filepath

    if group_path is not None and not group_path.exists():
        logger.warning(f"No groups found at {group_path}")
        group_path = None

    return group_path


def _dict_to_groups(data: dict[str, Any]) -> GroupConfiguration:
    config = GroupConfiguration(
        layout=data.get("layout", "monadtall"),
        decoration=data.get("decoration", None),
        groups=data.get("group", DEFAULT_GROUPS),
    )
    return config


def load_groups(filepath: Path | None = None) -> GroupConfiguration:
    group_path = _group_path(filepath)
    data = read_yaml(group_path)
    if data is None:
        group_data = {}
    else:
        group_data = data | {"path": group_path}
    return _dict_to_groups(group_data)
