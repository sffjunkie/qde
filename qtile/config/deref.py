from collections.abc import Mapping
from typing import Any, Iterable, Callable


def deref_data(
    data: dict,
    lookup: Mapping,
    is_dereferrable: Callable[[Any], bool] | None = None,
) -> dict[str, Any]:
    result = {}
    new_value: Any
    for name, value in data.items():
        if isinstance(value, dict):
            new_value = deref_data(value, lookup, is_dereferrable)
        elif not isinstance(value, str) and isinstance(value, Iterable):
            new_value = [lookup.get(item, item) for item in value]
        elif is_dereferrable is None or is_dereferrable(value):
            new_value = lookup.get(value, value)
        else:
            new_value = value

        result[name] = new_value

    return result
