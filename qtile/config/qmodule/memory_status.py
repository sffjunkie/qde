from libqtile.lazy import lazy  # type: ignore
from libqtile.widget import base  # type: ignore
from qtile_extras.widget import Memory  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from ..qwidget.icon import MDIcon
from ..terminal import terminal_from_env, terminal_run_command
from .base import WidgetModule
from .context import ModuleContext


class MemoryStatus(WidgetModule):
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

        system_status = terminal_run_command(terminal_from_env(), ["htop"])

        memory_props = {
            "format": "{MemUsed:6.0f}M/{MemTotal:.0f}M",
            "font": self.context.text_font_family,
            "fontsize": self.context.text_font_size,
            "padding": 8,
            "background": f"{background_color}00",
            "mouse_callbacks": {
                "Button1": lazy.spawn(system_status),
            },
        }

        props = self.context.merge_parameters(
            memory_props,
            self.context.props.pop("memory", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        memory = Memory(**props)

        icon_props = {
            "name": "memory",
            "font": self.context.icon_font_family,
            "fontsize": self.context.icon_font_size,
            "padding": 8,
            "background": f"{background_color}00",
            "mouse_callbacks": {
                "Button1": lazy.spawn(system_status),
            },
        }

        props = self.context.merge_parameters(
            icon_props,
            self.context.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        icon = MDIcon(**props)

        return [icon, memory]
