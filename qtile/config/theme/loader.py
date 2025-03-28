from pathlib import Path
from typing import Any, cast

from libqtile.log_utils import logger  # type: ignore

from ..fs import read_yaml, user_config_dir
from .default import (
    DEFAULT_COLOR,
    DEFAULT_EXTENSION,
    DEFAULT_LAYOUT,
    DEFAULT_WIDGET,
    DEFAULT_FONT,
    DEFAULT_BAR,
)
from .deref import deref_color
from .palette import (
    theme_base16_color_palette,
    theme_named_color_palette,
)
from .typedef import NamedColors, Theme


def _theme_path(filepath: Path | None = None) -> Path | None:
    theme_path: Path | None
    if filepath is not None and filepath.is_absolute():
        theme_path = filepath
    else:
        if filepath is None:
            filepath = Path("theme.yaml")

        theme_path = user_config_dir() / filepath

    if not theme_path.exists():
        logger.warning(f"No theme found in {theme_path}")
        theme_path = None

    return theme_path


def _dict_to_theme(data: dict[str, Any]):
    theme: Theme = {
        "bar": data.get("bar", DEFAULT_BAR),
        "color": data.get("color", DEFAULT_COLOR),
        "extension": data.get("extension", DEFAULT_EXTENSION),
        "font": data.get("font", DEFAULT_FONT),
        "layout": data.get("layout", DEFAULT_LAYOUT),
        "logo": data.get("logo", None),
        "path": data.get("path", None),
        "widget": data.get("widget", DEFAULT_WIDGET),
    }
    return theme


def _user_theme(filepath: Path | None) -> Theme:
    user_theme_path = _theme_path(filepath)
    theme_data = read_yaml(user_theme_path)
    if theme_data is None:
        user_theme_data = {}
    else:
        user_theme_data = theme_data | {"path": user_theme_path}
    return _dict_to_theme(user_theme_data)


def load_theme(filepath: Path | None = None) -> Theme:
    user_theme = _user_theme(filepath)

    base16_colors = theme_base16_color_palette(user_theme)
    # logger.warning(f"base16_colors: {base16_colors}")

    named_colors = theme_named_color_palette(user_theme)
    # logger.warning(f"named_colors: {named_colors}")

    updated_colors = deref_color(
        dict(named_colors),
        base16_colors,
    )
    named_colors = named_colors | cast(NamedColors, updated_colors)

    color = user_theme["color"]
    color["base16"]["palette"] = base16_colors
    color["named"] = named_colors

    widget = user_theme["widget"]
    widget = widget | deref_color(widget, base16_colors, named_colors)

    extension = user_theme["extension"]
    extension = extension | deref_color(extension, base16_colors, named_colors)

    layout = user_theme["layout"]
    layout = layout | deref_color(layout, base16_colors, named_colors)

    theme_def = Theme(
        path=user_theme["path"],
        bar=user_theme["bar"],
        color=color,
        extension=extension,
        font=user_theme["font"],
        layout=layout,
        logo=user_theme["logo"],
        widget=widget,
    )

    return theme_def
