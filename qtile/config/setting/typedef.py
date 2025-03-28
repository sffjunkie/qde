from typing import TypedDict, Any, NotRequired


class Apps(TypedDict):
    terminal: str

    app_launcher: str | None
    brain: str | None
    browser: str | None
    code: str | None
    system_menu: str | None
    user_menu: str | None
    volume: str | None
    wallpaper: str | None

    clipboard_copy: str | None
    clipboard_delete: str | None


class MusicController(TypedDict):
    next: str
    play: str
    previous: str
    stop: str
    toggle: str


class VolumeController(TypedDict):
    down: str
    mute: str
    toggle: str
    up: str


class Controllers(TypedDict):
    music: MusicController | None
    volume: VolumeController | None


class Devices(TypedDict):
    net: str


class Keys(TypedDict):
    alt: str
    cmd: str
    ctrl: str
    hyper: str
    shift: str


GroupOptions = dict[str, Any]
GroupName = str


class GroupDefinition(TypedDict):
    name: str
    options: GroupOptions
    matches: NotRequired[list[str]]


Groups = list[GroupDefinition]


class Settings(TypedDict):
    app: Apps
    device: Devices
    key: Keys
    controller: Controllers
    group: Groups
