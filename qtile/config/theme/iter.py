from itertools import cycle
from typing import Iterator

from ..color import contrast_color
from .model.default import DEFAULT_NAMED_COLORS
from .model import Theme


def _widget_fg_iter(theme: Theme) -> Iterator:
    def fg_cycle(iterable, fg_light: str, fg_dark: str) -> Iterator:
        saved = []
        for element in iterable:
            fg = contrast_color(element, fg_light, fg_dark)
            yield fg
            saved.append(fg)

        while saved:
            for element in saved:
                yield element

    return fg_cycle(
        theme.color.named.widget_bg or DEFAULT_NAMED_COLORS["widget_bg"],
        theme.color.named.widget_fg_light or DEFAULT_NAMED_COLORS["fg_light"],
        theme.color.named.widget_fg_dark or DEFAULT_NAMED_COLORS["fg_dark"],
    )


def _widget_bg_iter(theme: Theme) -> Iterator:
    return cycle(theme.color.named.widget_bg or DEFAULT_NAMED_COLORS["widget_bg"])


def widget_color_iter(theme: Theme) -> Iterator[tuple[str, str]]:
    bg_iter = _widget_bg_iter(theme)
    fg_iter = _widget_fg_iter(theme)

    while True:
        fg = next(fg_iter)
        bg = next(bg_iter)
        yield fg, bg
