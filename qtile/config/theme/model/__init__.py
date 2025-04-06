from pathlib import Path

from pydantic import BaseModel

from .color import Color
from .bar import Bars
from .font import Fonts
from .window import WindowFloating, WindowTiled
from .extension import Extension
from .widget import Widget


class Theme(BaseModel):
    bar: Bars
    color: Color
    extension: Extension
    font: Fonts
    logo: str | None
    path: Path | None
    widget: Widget
    window_floating: WindowFloating
    window_tiled: WindowTiled
