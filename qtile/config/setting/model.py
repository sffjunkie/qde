from pydantic import BaseModel

from .input.model import InputConfiguration
from .group.model import GroupConfiguration
from .default import DEFAULT_DEVICE, DEFAULT_KEY, DEFAULT_APP


class Apps(BaseModel):
    terminal: str = DEFAULT_APP["terminal"]

    app_launcher: str | None = None
    brain: str | None = None
    browser: str | None = None
    code: str | None = None
    system_menu: str | None = None
    user_menu: str | None = None
    volume: str | None = None
    wallpaper: str | None = None

    clipboard_copy: str | None = None
    clipboard_delete: str | None = None


class MusicController(BaseModel):
    next: str
    play: str
    previous: str
    stop: str
    toggle: str


class VolumeController(BaseModel):
    down: str
    mute: str
    toggle: str
    up: str


class Controllers(BaseModel):
    music: MusicController | None = None
    volume: VolumeController | None = None


class Devices(BaseModel):
    net: str = DEFAULT_DEVICE["net"]


class Keys(BaseModel):
    alt: str = DEFAULT_KEY["alt"]
    cmd: str = DEFAULT_KEY["cmd"]
    ctrl: str = DEFAULT_KEY["ctrl"]
    hyper: str = DEFAULT_KEY["hyper"]
    shift: str = DEFAULT_KEY["shift"]


class Settings(BaseModel):
    app: Apps
    device: Devices
    key: Keys
    controller: Controllers | None = None
    group: GroupConfiguration | None = None
    input: InputConfiguration | None = None
