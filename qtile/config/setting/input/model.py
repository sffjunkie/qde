from enum import StrEnum, auto
from pydantic import BaseModel


class Keyboard(BaseModel):
    kb_layout: str | None = None
    kb_options: str | None = None
    kb_variant: str | None = None
    kb_repeat_rate: int = 25
    kb_repeat_delay: int = 600


class AccelerationProfile(StrEnum):
    adaptive = auto()
    flat = auto()


class ClickMethod(StrEnum):
    none = auto()
    button_areas = auto()
    clickfinger = auto()


class ScrollMethod(StrEnum):
    none = auto()
    two_finger = auto()
    edge = auto()
    on_button_down = auto()


class TapButtonMap(StrEnum):
    lrm = auto()
    lmr = auto()


class Pointer(BaseModel):
    accel_profile: AccelerationProfile | None = None
    click_method: ClickMethod | None = None
    drag: bool | None = None
    drag_lock: bool | None = None
    left_handed: bool | None = None
    middle_emulation: bool | None = None
    natural_scroll: bool | None = None
    pointer_accel: float | None = None
    scroll_button: str | None = None
    scroll_method: ScrollMethod | None = None
    tap: bool | None = None
    tap_button_map: TapButtonMap | None = None


class InputConfiguration(BaseModel):
    keyboard: dict[str, Keyboard]
    pointer: dict[str, Pointer]
