from pathlib import Path
from typing import Any

from libqtile.log_utils import logger  # type: ignore

from ..fs import read_yaml, user_config_dir
from .typedef import Settings
from .default import DEFAULT_APP, DEFAULT_DEVICE, DEFAULT_KEY, DEFAULT_GROUP


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
    app = data.get("app", {})
    device = data.get("device", {})
    controller = data.get("controller", {})
    key = data.get("key", {})

    settings: Settings = {
        "app": {
            "terminal": app.get("terminal", DEFAULT_APP["terminal"]),
            "app_launcher": app.get("app_launcher", DEFAULT_APP["app_launcher"]),
            "brain": app.get("brain", DEFAULT_APP["brain"]),
            "browser": app.get("browser", DEFAULT_APP["browser"]),
            "clipboard_copy": app.get("cliboard_copy", DEFAULT_APP["clipboard_copy"]),
            "clipboard_delete": app.get(
                "cliboard_delete", DEFAULT_APP["clipboard_delete"]
            ),
            "code": app.get("code", DEFAULT_APP["code"]),
            "system_menu": app.get("system_menu", DEFAULT_APP["system_menu"]),
            "user_menu": app.get("user_menu", DEFAULT_APP["user_menu"]),
            "volume": app.get("volume", DEFAULT_APP["volume"]),
            "wallpaper": app.get("wallpaper", DEFAULT_APP["wallpaper"]),
        },
        "device": {
            "net": device.get("net", DEFAULT_DEVICE["net"]),
        },
        "controller": {
            "music": controller.get("music", None),
            "volume": controller.get("volume", None),
        },
        "group": data.get("group", DEFAULT_GROUP),
        "key": {
            "alt": key.get("alt", DEFAULT_KEY["alt"]),
            "cmd": key.get("cmd", DEFAULT_KEY["cmd"]),
            "ctrl": key.get("ctrl", DEFAULT_KEY["ctrl"]),
            "hyper": key.get("hyper", DEFAULT_KEY["hyper"]),
            "shift": key.get("shift", DEFAULT_KEY["shift"]),
        },
    }

    return settings


def load_settings(filepath: Path | None = None) -> Settings:
    settings_path = _settings_path(filepath)
    data = read_yaml(settings_path)
    if data is None:
        settings_data = {}
    else:
        settings_data = data | {"path": settings_path}
    return _dict_to_settings(settings_data)
