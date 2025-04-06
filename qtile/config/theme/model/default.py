DEFAULT_FONT_SIZE = 12
DEFAULT_TEXT_FONT = "DejaVu Sans Mono"
DEFAULT_ICON_FONT = "Hack Nerd Font Mono"
DEFAULT_LOGO_FONT = "Hack Nerd Font Mono"

DEFAULT_MARGIN = 4
DEFAULT_PADDING = 0
DEFAULT_BORDER_WIDTH = 3

DEFAULT_FONTS = {
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
DEFAULT_BASE16_PALETTE = {
    "base00": "#32302F",  # ----
    "base01": "#3C3836",  # ---
    "base02": "#504945",  # --
    "base03": "#665C54",  # -
    "base04": "#BDAE93",  # +
    "base05": "#D5C4A1",  # ++
    "base06": "#EBDBB2",  # +++
    "base07": "#FBF1C7",  # ++++
    "base08": "#FB4934",  # red
    "base09": "#FE8019",  # orange
    "base0A": "#FABD2F",  # yellow
    "base0B": "#B8BB26",  # green
    "base0C": "#8EC07C",  # aqua/cyan
    "base0D": "#83A598",  # blue
    "base0E": "#D3869B",  # purple
    "base0F": "#D65D0E",  # brown
}

DEFAULT_BASE16 = {
    "palette": DEFAULT_BASE16_PALETTE,
    "scheme_dir": None,
    "scheme_name": None,
}

DEFAULT_NAMED_COLORS = {
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
    "window_border_normal": DEFAULT_BASE16_PALETTE["base07"],
    "window_border_focus": DEFAULT_BASE16_PALETTE["base07"],
    "window_border_width": 3,
}

DEFAULT_COLOR = {
    "base16": DEFAULT_BASE16,
    "named": DEFAULT_NAMED_COLORS,
}

DEFAULT_BAR = {
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
    "left": None,
    "right": None,
}

DEFAULT_BAR_EXTENSION = {
    "font": DEFAULT_TEXT_FONT,
    "fontsize": DEFAULT_FONT_SIZE,
    "foreground": DEFAULT_BASE16_PALETTE["base00"],
    "background": DEFAULT_NAMED_COLORS["widget_bg"][0],
}

DEFAULT_WIDGET = {
    "font": DEFAULT_TEXT_FONT,
    "fontsize": DEFAULT_FONT_SIZE,
    "margin": 0,
    "padding": 0,
    "foreground": DEFAULT_BASE16_PALETTE["base00"],
    "background": DEFAULT_NAMED_COLORS["widget_bg"][0],
}

DEFAULT_WINDOW = {
    "margin": DEFAULT_MARGIN,
    "border_width": DEFAULT_BORDER_WIDTH,
    "border_focus": DEFAULT_NAMED_COLORS["window_border_focus"],
    "border_normal": DEFAULT_NAMED_COLORS["window_border_normal"],
}

DEFAULT_FLOATING = {
    "border_width": DEFAULT_BORDER_WIDTH,
    "border_focus": DEFAULT_NAMED_COLORS["window_border_focus"],
    "border_normal": DEFAULT_NAMED_COLORS["window_border_normal"],
}

DEFAULT_THEME = {
    "bar": DEFAULT_BAR,
    "color": DEFAULT_COLOR,
    "extension": DEFAULT_BAR_EXTENSION,
    "font": DEFAULT_FONTS,
    "logo": None,
    "path": None,
    "widget": DEFAULT_WIDGET,
    "window_floating": DEFAULT_WINDOW,
    "window_tiled": DEFAULT_WINDOW,
}
