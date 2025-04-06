from pydantic import BaseModel

from .default import DEFAULT_NAMED_COLORS, DEFAULT_BASE16_PALETTE


class Base16Palette(BaseModel):
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


class Base16(BaseModel):
    palette: Base16Palette = Base16Palette.model_validate(DEFAULT_BASE16_PALETTE)
    scheme_name: str | None = None
    scheme_dir: str | None = None


class NamedColor(BaseModel):
    group_current_fg: str = DEFAULT_NAMED_COLORS["group_current_fg"]
    group_current_bg: str = DEFAULT_NAMED_COLORS["group_current_bg"]
    group_active_fg: str = DEFAULT_NAMED_COLORS["group_active_fg"]
    group_active_bg: str = DEFAULT_NAMED_COLORS["group_active_bg"]
    group_inactive_fg: str = DEFAULT_NAMED_COLORS["group_inactive_fg"]
    group_inactive_bg: str = DEFAULT_NAMED_COLORS["group_inactive_bg"]

    panel_fg: str = DEFAULT_NAMED_COLORS["panel_fg"]
    panel_bg: str = DEFAULT_NAMED_COLORS["panel_bg"]

    widget_bg: list[str] = DEFAULT_NAMED_COLORS["widget_bg"]
    widget_fg_dark: str = DEFAULT_NAMED_COLORS["widget_fg_dark"]
    widget_fg_light: str = DEFAULT_NAMED_COLORS["widget_fg_light"]

    window_border_focus: str = DEFAULT_NAMED_COLORS["window_border_focus"]
    window_border_normal: str = DEFAULT_NAMED_COLORS["window_border_normal"]
    window_border_width: int = DEFAULT_NAMED_COLORS["window_border_width"]


class Color(BaseModel):
    base16: Base16
    named: NamedColor
