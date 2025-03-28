from libqtile import layout  # type: ignore
from libqtile.backend.wayland.inputs import InputConfig  # type: ignore
from libqtile.config import Screen  # type: ignore

from . import bars
from . import floating
from . import scratchpad
from . import wallpaper
from .debug import show_runtime_info
from .group import build_groups
from .input.keyboard import build_keys
from .input.mouse import build_mouse_buttons
from .secret.loader import load_secrets
from .setting.loader import load_settings
from .theme.loader import load_theme

show_runtime_info()

secrets = load_secrets()
settings = load_settings()

theme = load_theme()

bar_defs = bars.build_bars(settings=settings, theme=theme)
screens = [
    Screen(
        top=bar_defs["top"],
        bottom=bar_defs["bottom"],
        left=bar_defs["left"],
        right=bar_defs["right"],
        wallpaper=wallpaper.get_wallpaper()[0],
        wallpaper_mode="fill",
    ),
]

groups = build_groups(settings) + scratchpad.build_scratchpads(settings)

keys = build_keys(settings) + scratchpad.build_keys(settings)
mouse = build_mouse_buttons(settings)

floating_layout = floating.build_layout(theme=theme)
layouts = [
    layout.MonadTall(**theme["layout"]),
    layout.Max(**theme["layout"]),
]

auto_fullscreen = True
bring_front_click = "floating_only"
cursor_warp = False
extension_defaults = theme["extension"].copy()
focus_on_window_activation = "smart"
follow_mouse_focus = False
widget_defaults = theme["widget"].copy()
wmname = "QTile"


# to get ids use `qtile cmd-obj -o core -f get_inputs`
wl_input_rules = {
    "1452:591:Keychron Keychron K1": InputConfig(
        kb_layout="hyper_super",  # configuration/module/home/wayland/keyboard/hyper_super
        kb_options="altwin:swap_lalt_lwin",
    ),
    "1133:45082:MX Anywhere 2S Mouse": InputConfig(natural_scroll=True),
    "1386:828:Wacom Intuos PT S 2 Finger": InputConfig(tap=True),
}

wl_xcursor_size = 32
