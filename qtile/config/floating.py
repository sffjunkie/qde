from libqtile import layout  # type: ignore
from libqtile.config import Match, _Match  # type: ignore

from .theme.model import Theme

wmclass_float = [
    "com.github.wwmm.easyeffects",
    "org.pulseaudio.pavucontrol",
    "org.gnome.Calculator",
    "org.gnome.Characters",
    "Pinentry",
    "ssh-askpass",
    "waypaper",
    "yubico.org.",
]


def float_rules() -> list[_Match]:
    return [
        Match(wm_class=float_match) for float_match in wmclass_float
    ] + layout.Floating.default_float_rules


def build_layout(theme: Theme) -> layout.Floating:
    return layout.Floating(
        float_rules=float_rules(),
        border_normal=theme.window_floating.border_normal,
        border_focus=theme.window_floating.border_focus,
    )
