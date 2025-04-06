from qtile.config.theme.model import Theme
from config.theme.iter import _widget_bg_iter, _widget_fg_iter, widget_color_iter


def test_default_bg_iter(default_theme: Theme):
    iter = _widget_bg_iter(default_theme)
    assert next(iter) == "#D65D0E"
    assert next(iter) == "#D65D0E"
    assert next(iter) == "#D65D0E"


def test_bg_iter(theme: Theme):
    iter = _widget_bg_iter(theme)
    assert next(iter) == "#8FBCBB"
    assert next(iter) == "#ECEFF4"
    assert next(iter) == "#8FBCBB"


def test_default_fg_iter(default_theme: Theme):
    iter = _widget_fg_iter(default_theme)
    assert next(iter) == "#D8DEE9"


def test_fg_iter(theme: Theme):
    iter = _widget_fg_iter(theme)
    assert next(iter) == "#2E3440"


def test_widget_color_iter(theme: Theme):
    iter = widget_color_iter(theme)
    assert next(iter) == ("#2E3440", "#8FBCBB")
    assert next(iter) == ("#2E3440", "#ECEFF4")
    assert next(iter) == ("#2E3440", "#8FBCBB")
