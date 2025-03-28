from libqtile.lazy import lazy  # type: ignore
from libqtile.widget import base  # type: ignore
from qtile_extras.widget import PulseVolume  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from ..qwidget.icon import MDIcon
from .base import WidgetModule
from .context import ModuleContext


class VolumeStatus(WidgetModule):
    def __init__(
        self,
        context: ModuleContext,
    ):
        self.context = context

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.context.props.get(
            "background", self.context.bar.background
        )

        decorations = None
        if group_id != -1:
            decorations = [
                RectDecoration(
                    colour=f"{background_color}{self.context.bar.opacity_str}",
                    radius=5,
                    filled=True,
                    group=True,
                    group_id=group_id,
                )
            ]

        volume_text_props = {
            "name": "bar_volume",
            "volume_app": "volumectl app",
            "mute_format": "   M",
            "unmute_format": "{volume:>3}%",
            "menu_font": self.context.text_font_family,
            "menu_fontsize": int(self.context.text_font_size * 0.8),
            "menu_width": 500,
            "menu_offset_x": -250,
            "padding": 8,
            "font": self.context.text_font_family,
            "fontsize": self.context.text_font_size,
            "background": f"{background_color}00",
        }

        props = self.context.merge_parameters(
            volume_text_props,
            self.context.props.pop("volume", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        volume_text = PulseVolume(**props)

        volume_icon_props = {
            "name": "volume",
            "font": self.context.icon_font_family,
            "fontsize": self.context.icon_font_size,
            "padding": 8,
            "background": f"{background_color}00",
            "mouse_callbacks": {
                "Button1": lazy.widget["bar_volume"].mute(),
                "Button4": lazy.widget["bar_volume"].increase_vol(),
                "Button5": lazy.widget["bar_volume"].decrease_vol(),
            },
        }

        props = self.context.merge_parameters(
            volume_icon_props,
            self.context.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        volume_icon = MDIcon(**props)

        widgets = [volume_text, volume_icon]
        return widgets
