from pathlib import Path

from qtile.config.theme.model import Theme
from config.theme.loader import load_theme


def test_theme_loader_load_default():
    p = Path("/tmp/theme.notthere")
    theme = load_theme(p)
    assert theme.path is None
    assert theme.font["icon"].family == "Hack Nerd Font Mono"
    assert len(theme.color.named.widget_bg) == 1

    assert theme.color.base16.palette.base00 == "#32302F"


def test_theme_loader_load(theme: Theme):
    assert theme.path == Path(__file__).parent.parent / Path("data/theme.yaml")
    assert theme.font["text"].family == "JetBrainsMono Nerd Font"
    assert theme.color.named.widget_bg is not None
    assert len(theme.color.named.widget_bg) == 2

    assert theme.color.base16.scheme_name == "nord"
    assert theme.color.base16.palette.base00 == "#2E3440"
