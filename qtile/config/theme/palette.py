import os
from pathlib import Path

import yaml  # type: ignore

from .model.default import DEFAULT_BASE16_PALETTE, DEFAULT_NAMED_COLORS


def _load_base16_color_scheme(
    scheme_file: str, scheme_folder: str | None = None
) -> dict | None:
    if scheme_folder is None:
        xdg_data_home = os.environ.get("XDG_DATA_HOME", None)
        if xdg_data_home is not None:
            search_folder = Path(xdg_data_home) / "base16" / "schemes"
        else:
            search_folder = Path(__file__).parent / "schemes"
    else:
        search_folder = Path(scheme_folder)

    scheme_path = Path(scheme_file)
    if scheme_path.suffix != ".yaml":
        scheme_path = scheme_path.with_suffix(".yaml")

    for file_path in search_folder.rglob(os.path.join("**", "*.yaml")):
        if file_path.name.endswith(scheme_path.name):
            with open(file_path, "r") as fp:
                colors = yaml.load(fp, Loader=yaml.SafeLoader)
                return colors["palette"]

    return None


def theme_base16_color_palette(theme_data: dict) -> dict:
    if theme_data["color"] is None or theme_data["color"].get("base16", None) is None:
        return DEFAULT_BASE16_PALETTE  # type: ignore

    base16_palette = None
    if theme_data["color"]["base16"].get("palette", None) is None:
        scheme_dir = theme_data["color"]["base16"].get("scheme_dir", None)
        scheme_name = theme_data["color"]["base16"].get("scheme_name", None)
        if scheme_name is not None and scheme_dir is not None:
            base16_palette = _load_base16_color_scheme(scheme_name, scheme_dir)

    if base16_palette is None:
        base16_palette = DEFAULT_BASE16_PALETTE

    return base16_palette  # type: ignore


def theme_named_color_palette(
    theme_data: dict,
) -> dict:
    if theme_data["color"] is None or theme_data["color"]["named"] is None:
        named_colors = DEFAULT_NAMED_COLORS
    else:
        named_colors = DEFAULT_NAMED_COLORS | theme_data["color"]["named"]

    return named_colors
