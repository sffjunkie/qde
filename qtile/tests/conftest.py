from pathlib import Path
from pytest import fixture

from qtile.config.setting.input.model import InputConfiguration
from config.setting.input.loader import load_inputs
from qtile.config.setting.model import Settings
from config.setting.loader import load_settings
from qtile.config.theme.model import Theme
from config.theme.loader import load_theme


@fixture
def settings() -> Settings:
    data_dir = Path(__file__).parent
    p = data_dir / "data" / "settings.yaml"
    return load_settings(p)


@fixture
def default_theme() -> Theme:
    return load_theme()


@fixture
def theme() -> Theme:
    data_dir = Path(__file__).parent
    p = data_dir / "data" / "theme.yaml"
    return load_theme(p)


@fixture
def inputs() -> InputConfiguration:
    data_dir = Path(__file__).parent
    p = data_dir / "data" / "input.yaml"
    return load_inputs(p)
