from pathlib import Path

from config.theme.typedef import Theme
from config.theme.loader import load_theme


def test_theme_loader_load_default():
    p = Path("/tmp/theme.notthere")
    theme = load_theme(p)
    assert theme["path"] is None
    assert theme["font"]["icon"]["family"] == "Hack Nerd Font Mono"
    assert len(theme["color"]["named"]["widget_bg"]) == 1


def test_theme_loader_load(theme: Theme):
    assert theme["path"] == Path(__file__).parent / Path("data/theme.yaml")
    assert theme["font"]["text"]["family"] == "JetBrainsMono Nerd Font"
    assert len(theme["color"]["named"]["widget_bg"]) == 2
