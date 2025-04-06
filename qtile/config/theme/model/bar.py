from pydantic import BaseModel


from .default import DEFAULT_FONT_SIZE


class BarDefinition(BaseModel):
    height: int = DEFAULT_FONT_SIZE + 8
    opacity: float = 1.0
    margin: tuple[int, int, int, int] = (0, 0, 0, 0)


class Bars(BaseModel):
    top: BarDefinition | None = None
    bottom: BarDefinition | None = None
    left: BarDefinition | None = None
    right: BarDefinition | None = None
