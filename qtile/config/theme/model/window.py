from pydantic import BaseModel

from .default import DEFAULT_WINDOW


class WindowTiled(BaseModel):
    margin: int = DEFAULT_WINDOW["margin"]
    border_width: int = DEFAULT_WINDOW["border_width"]
    border_focus: str = DEFAULT_WINDOW["border_focus"]
    border_normal: str = DEFAULT_WINDOW["border_normal"]


class WindowFloating(BaseModel):
    border_width: int = DEFAULT_WINDOW["border_width"]
    border_focus: str = DEFAULT_WINDOW["border_focus"]
    border_normal: str = DEFAULT_WINDOW["border_normal"]
