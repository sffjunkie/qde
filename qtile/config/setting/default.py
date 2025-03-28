from .typedef import Apps, Keys, Devices

DEFAULT_APP: Apps = {
    "terminal": "xterm",
    "brain": None,
    "browser": None,
    "code": None,
    "volume": None,
    "user_menu": None,
    "system_menu": None,
    "app_launcher": None,
    "clipboard_copy": None,
    "clipboard_delete": None,
    "wallpaper": None,
}

DEFAULT_DEVICE: Devices = {
    "net": "eth0",
}

DEFAULT_KEY: Keys = {
    "alt": "mod1",
    "ctrl": "control",
    "hyper": "mod3",
    "shift": "shift",
    "cmd": "mod4",
}


DEFAULT_GROUP = [
    {
        "name": "WWW",
        "options": {"layout": "monadtall"},
    }
]
