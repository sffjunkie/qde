from pathlib import Path

from libqtile.log_utils import logger  # type: ignore

from ..fs import read_yaml, user_config_dir
from .model.default import (
    DEFAULT_NAMED_COLORS,
    DEFAULT_BAR_EXTENSION,
    DEFAULT_WINDOW,
    DEFAULT_WIDGET,
    DEFAULT_BASE16,
    DEFAULT_FLOATING,
    DEFAULT_THEME,
    DEFAULT_FONTS,
    DEFAULT_BAR,
)
from .deref import deref_color
from .palette import (
    theme_base16_color_palette,
    theme_named_color_palette,
)
from .model import Theme


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


def _theme_data(filepath: Path | None) -> dict:
    theme_data = read_yaml(filepath)
    if not theme_data:
        user_theme_data = DEFAULT_THEME
    else:
        user_theme_data = DEFAULT_THEME | theme_data | {"path": filepath}
    return user_theme_data


def load_theme(filepath: Path | None = None) -> Theme:
    user_theme_path = _theme_path(filepath)
    user_theme = _theme_data(user_theme_path)

    base16_palette = theme_base16_color_palette(user_theme)

    if (
        user_theme.get("color", None) is None
        or user_theme["color"].get("base16", None) is None
    ):
        b16 = DEFAULT_BASE16
    else:
        b16 = (
            DEFAULT_BASE16 | user_theme["color"]["base16"] | {"palette": base16_palette}
        )

    named_colors = theme_named_color_palette(user_theme)
    named_colors = named_colors | deref_color(
        data=named_colors,
        base16_colors=base16_palette,
    )

    if user_theme["color"].get("named", None) is None:
        nc = DEFAULT_NAMED_COLORS
    else:
        nc = DEFAULT_NAMED_COLORS | named_colors

    color = {"base16": b16, "named": nc}

    widget_dict = DEFAULT_WIDGET | user_theme["widget"]
    widget = widget_dict | deref_color(
        widget_dict,
        base16_colors=base16_palette,
        named_colors=named_colors,
    )

    extension_dict = DEFAULT_BAR_EXTENSION | user_theme["extension"]
    extension = extension_dict | deref_color(
        data=extension_dict,
        base16_colors=base16_palette,
        named_colors=named_colors,
    )

    wt_dict = DEFAULT_WINDOW | user_theme["window_tiled"]
    window_tiled = wt_dict | deref_color(
        data=wt_dict,
        base16_colors=base16_palette,
        named_colors=named_colors,
    )

    wf_dict = DEFAULT_FLOATING | user_theme["window_floating"]
    window_floating = wf_dict | deref_color(
        data=wf_dict,
        base16_colors=base16_palette,
        named_colors=named_colors,
    )

    bar = DEFAULT_BAR | user_theme["bar"]
    font = DEFAULT_FONTS | user_theme["font"]

    theme_def = Theme.model_validate(
        {
            "bar": bar,
            "color": color,
            "extension": extension,
            "font": font,
            "logo": user_theme["logo"],
            "path": user_theme_path,
            "widget": widget,
            "window_floating": window_floating,
            "window_tiled": window_tiled,
        }
    )

    return theme_def
