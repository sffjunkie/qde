from dataclasses import dataclass
from typing import Annotated

RGBColor = tuple[float, float, float]
RGBHex = str


@dataclass
class OpacityRange:
    min: float
    max: float


Opacity = Annotated[float, OpacityRange(min=0.0, max=1.0)]
