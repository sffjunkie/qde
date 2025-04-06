from libqtile import layout  # type: ignore
from libqtile.config import Screen  # type: ignore

from . import bars
from . import floating
from . import scratchpad
from . import wallpaper
from .debug import show_runtime_info
from .builder.group import build_groups
from .setting.input.loader import load_inputs
from .builder.keys import build_keys
from .builder.buttons import build_buttons
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
mouse = build_buttons(settings)

floating_layout = floating.build_layout(theme=theme)

if theme.window_tiled is not None:
    layout_params = dict(theme.window_tiled)
else:
    layout_params = {}

layouts = [
    layout.MonadTall(**layout_params),
    layout.Max(**layout_params),
]

auto_fullscreen = True
bring_front_click = "floating_only"
cursor_warp = False
extension_defaults = theme.extension
focus_on_window_activation = "smart"
follow_mouse_focus = False
widget_defaults = theme.widget
wmname = "QTile"


# to get ids use `qtile cmd-obj -o core -f get_inputs`
wl_input_rules = load_inputs()

wl_xcursor_size = 32
