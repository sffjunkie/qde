from pydantic import BaseModel

from .default import (
    DEFAULT_TEXT_FONT,
    DEFAULT_FONT_SIZE,
    DEFAULT_BASE16_PALETTE,
    DEFAULT_NAMED_COLORS,
)


class Extension(BaseModel):
    font: str = DEFAULT_TEXT_FONT
    fontsize: int = DEFAULT_FONT_SIZE
    foreground: str = DEFAULT_BASE16_PALETTE["base00"]
    background: str = DEFAULT_NAMED_COLORS["widget_bg"]
