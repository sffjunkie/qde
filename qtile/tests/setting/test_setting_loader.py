from pathlib import Path

from qtile.config.setting.model import Settings
from config.setting.loader import load_settings


def test_setting_loader_load_nonexistent():
    p = Path("/tmp/settings.notthere")
    settings = load_settings(p)
    assert settings.device.net == "eth0"


def test_setting_loader_load(settings: Settings):
    assert settings.device.net == "wlp3s0"
