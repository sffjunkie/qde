from typing import Literal

from qtile_extras.widget.decorations import PowerLineDecoration  # type: ignore

from ..color import opacity_to_str
from ..theme.typedef import Theme
from ..setting.typedef import Settings

BarPosition = Literal["top", "right", "bottom", "left"]


class BarContext:
    height: int
    margin: tuple[int, int, int, int]
    powerline_start: list[PowerLineDecoration]
    powerline_end: list[PowerLineDecoration]

    text_font_family: str
    text_font_size: int
    icon_font_family: str
    icon_font_size: int
    logo_font_family: str
    logo_font_size: int

    background: str
    opacity: float

    def __init__(
        self,
        position: BarPosition,
        settings: Settings,
        theme: Theme,
        props: dict = {},
    ):
        self.position = position
        self.settings = settings
        self.theme = theme
        self.props = props

        bar_props = theme["bar"].get(self.position, None)

        assert bar_props is not None

        self.height = props.get("height", bar_props["height"])
        self.margin = props.get("margin", bar_props["margin"])

        self.text_font_family = props.get(
            "text_font_family", theme["font"]["text"]["family"]
        )
        self.text_font_size = props.get("text_font_size", theme["font"]["text"]["size"])
        self.icon_font_family = props.get(
            "icon_font_family", theme["font"]["icon"]["family"]
        )
        self.icon_font_size = props.get("icon_font_size", theme["font"]["icon"]["size"])
        self.logo_font_family = props.get(
            "logo_font_family", theme["font"]["logo"]["family"]
        )
        self.logo_font_size = props.get("logo_font_size", theme["font"]["logo"]["size"])

        self.background = props.get(
            "background",
            bar_props.get("background", theme["color"]["named"]["panel_bg"]),
        )
        self.opacity = props.get("opacity", bar_props.get("opacity", 1.0))
        self.opacity_str = opacity_to_str(self.opacity)
        self.background_color = f"{self.background}{self.opacity_str}"

        powerline = bar_props.get("powerline", None)
        if powerline is not None:
            start = powerline.get("start", None)
            if start is not None:
                self.powerline_start = [PowerLineDecoration(path=start)]
                self.powerline_start = []

            if (end := powerline.get("end", None)) is not None:
                self.powerline_end = [PowerLineDecoration(path=end)]
            else:
                self.powerline_end = []

        else:
            self.powerline_start = []
            self.powerline_end = []
