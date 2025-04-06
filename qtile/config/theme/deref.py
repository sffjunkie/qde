from collections import ChainMap
from collections.abc import MutableMapping
from typing import Any

from ..color import is_color
from ..deref import deref_data


def is_dereferrable(value: Any):
    if value is None:
        return False

    return not isinstance(value, (int, float, bool)) and not is_color(value)


def deref_color(
    data: dict,
    base16_colors: dict[str, str],
    named_colors: dict | None = None,
) -> dict[str, Any]:
    base16 = base16_colors
    # if named_colors is not None:
    #     named = named_colors
    # else:
    #     named = {}

    lookup: MutableMapping[str, str]
    if named_colors is not None:
        lookup = ChainMap(base16, named_colors)
    else:
        lookup = base16

    d = deref_data(data, lookup, is_dereferrable)
    return d
