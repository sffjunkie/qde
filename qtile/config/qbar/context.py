from typing import Literal

from ..color import opacity_to_str
from ..theme.model.default import DEFAULT_FONT_SIZE
from ..theme.model import Theme
from ..setting.model import Settings

BarPosition = Literal["top", "bottom", "right", "left"]


class BarContext:
    height: int
    margin: tuple[int, int, int, int]

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

        bar_props = getattr(theme.bar, self.position, None)

        assert bar_props is not None

        self.height = getattr(props, "height", bar_props.height)
        self.margin = getattr(props, "margin", bar_props.margin)

        self.text_font_family = getattr(
            props, "text_font_family", theme.font["text"].family
        )
        theme_text_font_size = theme.font["text"].size or DEFAULT_FONT_SIZE
        self.text_font_size = getattr(props, "text_font_size", theme_text_font_size)
        self.icon_font_family = getattr(
            props, "icon_font_family", theme.font["icon"].family
        )
        theme_icon_font_size = theme.font["icon"].size or DEFAULT_FONT_SIZE
        self.icon_font_size = getattr(props, "icon_font_size", theme_icon_font_size)
        self.logo_font_family = getattr(
            props, "logo_font_family", theme.font["logo"].family
        )
        theme_logo_font_size = theme.font["logo"].size or DEFAULT_FONT_SIZE
        self.logo_font_size = getattr(props, "logo_font_size", theme_logo_font_size)

        self.background = props.get(
            "background",
            getattr(bar_props, "background", theme.color.named.panel_bg),
        )
        self.opacity = getattr(props, "opacity", bar_props.opacity)
        self.opacity_str = opacity_to_str(self.opacity)
        self.background_color = f"{self.background}{self.opacity_str}"
