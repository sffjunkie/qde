from libqtile.config import Click, Drag  # type: ignore
from libqtile.lazy import lazy  # type: ignore

from ..setting.typedef import Settings


def build_mouse_buttons(settings: Settings):
    cmd = settings["key"]["cmd"]
    return [
        Drag(
            [cmd],
            "Button1",
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [cmd],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click([cmd], "Button2", lazy.window.bring_to_front()),
    ]
