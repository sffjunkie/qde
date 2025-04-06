from dataclasses import dataclass
from enum import Enum, auto
from typing import Annotated, NamedTuple


@dataclass
class FloatRange:
    min: float
    max: float


ScreenFraction = Annotated[float, FloatRange(min=0.0, max=1.0)]


class Margins(NamedTuple):
    top: ScreenFraction
    right: ScreenFraction
    bottom: ScreenFraction
    left: ScreenFraction


Margin = ScreenFraction | Margins


@dataclass
class WindowPosition:
    x: float
    y: float
    width: float
    height: float


class WindowLocation(Enum):
    Left = auto()
    Right = auto()
    Top = auto()
    Bottom = auto()
    TopLeft = auto()
    TopCenter = auto()
    TopRight = auto()
    BottomLeft = auto()
    BottomCenter = auto()
    BottomRight = auto()
    Centered = auto()


class SizePreference(Enum):
    dimension = auto()
    margin = auto()
