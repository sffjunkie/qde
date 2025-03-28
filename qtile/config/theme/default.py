from .typedef import (
    Base16Palette,
    Base16,
    NamedColors,
    Colors,
    PropertyDefinitions,
    FontDefinitions,
    BarDefinitions,
)

DEFAULT_FONT_SIZE = 12
DEFAULT_TEXT_FONT = "DejaVu Sans Mono"
DEFAULT_ICON_FONT = "Hack Nerd Font Mono"
DEFAULT_LOGO_FONT = "Hack Nerd Font Mono"

DEFAULT_MARGIN = 4

DEFAULT_FONT: FontDefinitions = {
    "text": {
        "family": DEFAULT_TEXT_FONT,
        "size": DEFAULT_FONT_SIZE,
    },
    "icon": {
        "family": DEFAULT_ICON_FONT,
        "size": DEFAULT_FONT_SIZE,
    },
    "logo": {
        "family": DEFAULT_LOGO_FONT,
        "size": DEFAULT_FONT_SIZE,
    },
}

# gruvbox-dark-soft
DEFAULT_BASE16_PALETTE: Base16Palette = {
    "base00": "#32302f",  # ----
    "base01": "#3c3836",  # ---
    "base02": "#504945",  # --
    "base03": "#665c54",  # -
    "base04": "#bdae93",  # +
    "base05": "#d5c4a1",  # ++
    "base06": "#ebdbb2",  # +++
    "base07": "#fbf1c7",  # ++++
    "base08": "#fb4934",  # red
    "base09": "#fe8019",  # orange
    "base0A": "#fabd2f",  # yellow
    "base0B": "#b8bb26",  # green
    "base0C": "#8ec07c",  # aqua/cyan
    "base0D": "#83a598",  # blue
    "base0E": "#d3869b",  # purple
    "base0F": "#d65d0e",  # brown
}

DEFAULT_BASE16: Base16 = {
    "palette": DEFAULT_BASE16_PALETTE,
    "scheme_dir": None,
    "scheme_name": None,
}

DEFAULT_NAMED_COLORS: NamedColors = {
    "panel_fg": DEFAULT_BASE16_PALETTE["base04"],
    "panel_bg": DEFAULT_BASE16_PALETTE["base01"],
    "group_current_fg": DEFAULT_BASE16_PALETTE["base05"],
    "group_current_bg": DEFAULT_BASE16_PALETTE["base03"],
    "group_active_fg": DEFAULT_BASE16_PALETTE["base07"],
    "group_active_bg": DEFAULT_BASE16_PALETTE["base04"],
    "group_inactive_fg": DEFAULT_BASE16_PALETTE["base07"],
    "group_inactive_bg": DEFAULT_BASE16_PALETTE["base04"],
    "widget_bg": [
        DEFAULT_BASE16_PALETTE["base0F"],
    ],
    "widget_fg_dark": DEFAULT_BASE16_PALETTE["base00"],
    "widget_fg_light": DEFAULT_BASE16_PALETTE["base04"],
    "window_border": DEFAULT_BASE16_PALETTE["base06"],
}

DEFAULT_COLOR: Colors = {
    "base16": DEFAULT_BASE16,
    "named": DEFAULT_NAMED_COLORS,
}

DEFAULT_BAR: BarDefinitions = {
    "top": {
        "height": 22,
        "margin": (4, 4, 0, 4),
        "opacity": 1.0,
    },
    "bottom": {
        "height": 22,
        "margin": (0, 4, 4, 4),
        "opacity": 1.0,
    },
}

DEFAULT_EXTENSION: PropertyDefinitions = {
    "font": DEFAULT_TEXT_FONT,
    "fontsize": DEFAULT_FONT_SIZE,
    "foreground": DEFAULT_BASE16_PALETTE["base04"],
    "background": DEFAULT_BASE16_PALETTE["base00"],
}

DEFAULT_LAYOUT: PropertyDefinitions = {
    "margin": DEFAULT_MARGIN,
    "border_width": 3,
    "border_focus": DEFAULT_BASE16_PALETTE["base02"],
    "border_normal": DEFAULT_BASE16_PALETTE["base07"],
}

DEFAULT_WIDGET: PropertyDefinitions = {
    "font": DEFAULT_TEXT_FONT,
    "fontsize": DEFAULT_FONT_SIZE,
    "margin": 0,
    "padding": 0,
    "foreground": DEFAULT_BASE16_PALETTE["base00"],
    "background": DEFAULT_BASE16_PALETTE["base07"],
}
