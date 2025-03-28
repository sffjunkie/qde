from pathlib import Path
from typing import TypedDict, NotRequired

PropertyDefinitions = dict[str, str | int | float]


# region bar
class BarDefinition(TypedDict):
    height: int
    opacity: float
    margin: tuple[int, int, int, int]


class BarDefinitions(TypedDict):
    top: NotRequired[BarDefinition]
    bottom: NotRequired[BarDefinition]
    left: NotRequired[BarDefinition]
    right: NotRequired[BarDefinition]


# endregion

# region color
Color = str


class Base16Palette(TypedDict):
    base00: str
    base01: str
    base02: str
    base03: str
    base04: str
    base05: str
    base06: str
    base07: str
    base08: str
    base09: str
    base0A: str
    base0B: str
    base0C: str
    base0D: str
    base0E: str
    base0F: str


class Base16(TypedDict):
    palette: NotRequired[Base16Palette]
    scheme_name: str | None
    scheme_dir: str | None


class NamedColors(TypedDict):
    group_current_fg: Color
    group_current_bg: Color
    group_active_fg: Color
    group_active_bg: Color
    group_inactive_fg: Color
    group_inactive_bg: Color

    panel_fg: Color
    panel_bg: Color

    widget_bg: list[Color]
    widget_fg_dark: Color
    widget_fg_light: Color

    window_border: Color


class Colors(TypedDict):
    base16: Base16
    named: NamedColors


# endregion

# region font
FontType = str


class FontDefinition(TypedDict):
    family: str
    size: int


FontDefinitions = dict[FontType, FontDefinition]
# endregion


class Theme(TypedDict):
    bar: BarDefinitions
    color: Colors
    extension: PropertyDefinitions
    font: FontDefinitions
    layout: PropertyDefinitions
    logo: str | None
    path: Path | None
    widget: PropertyDefinitions
