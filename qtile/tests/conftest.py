from pathlib import Path
from pytest import fixture

from config.setting.typedef import Settings
from config.setting.loader import load_settings
from config.theme.typedef import Theme
from config.theme.loader import load_theme


@fixture
def settings() -> Settings:
    data_dir = Path(__file__).parent
    p = data_dir / "data" / "settings.yaml"
    return load_settings(p)


@fixture
def theme() -> Theme:
    data_dir = Path(__file__).parent
    p = data_dir / "data" / "theme.yaml"
    return load_theme(p)
