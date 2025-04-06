from typing import Literal

from pydantic import BaseModel

from .default import DEFAULT_FONT_SIZE

FontType = Literal["text", "icon", "logo", "weather"]


class FontDefinition(BaseModel):
    family: str
    size: int = DEFAULT_FONT_SIZE


Fonts = dict[FontType, FontDefinition]
