from typing import Any
from collections import ChainMap

from ..color import is_color
from ..deref import deref_data
from .typedef import Base16Palette, NamedColors


def is_dereferrable(value: Any):
    if value is None:
        return False

    return not isinstance(value, (int, float, bool)) and not is_color(value)


def deref_color(
    data: dict,
    base16_colors: Base16Palette,
    named_colors: NamedColors | None = None,
) -> dict[str, Any]:
    if named_colors is not None:
        lookup = ChainMap(dict(base16_colors), dict(named_colors))
    else:
        lookup = base16_colors

    d = deref_data(data, lookup, is_dereferrable)
    return d
