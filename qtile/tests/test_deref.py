from typing import Any
from config.deref import deref_data


def test_deref_int():
    data = {"a": 1}
    lookup = {1: 23}

    assert deref_data(data, lookup) == {"a": 23}


def test_deref_float():
    data = {"a": 1.4}
    lookup = {1.4: 23.0}

    assert deref_data(data, lookup) == {"a": 23.0}


def test_deref_string():
    data = {"a": "base00"}
    lookup = {"base00": "#000000"}

    assert deref_data(data, lookup) == {"a": "#000000"}


def test_deferrable():
    def is_defer(value: Any):
        return not isinstance(value, (int, float, bool))

    data = {"a": 1.4}
    lookup = {1.4: 23.0}

    assert deref_data(data, lookup, is_defer) == {"a": 1.4}


def test_deref_dict():
    data = {
        "a": "base01",
        "b": {"c": {"d": "base02"}},
    }
    lookup = {
        "base01": "#000000",
        "base02": "#FFFFFF",
    }

    new_data = deref_data(data, lookup)
    assert new_data == {
        "a": "#000000",
        "b": {
            "c": {
                "d": "#FFFFFF",
            }
        },
    }


def test_deref_list():
    data = {
        "a": "base01",
        "b": ["base01", "base02"],
    }
    lookup = {
        "base01": "#000000",
        "base02": "#FFFFFF",
    }

    new_data = deref_data(data, lookup)
    assert new_data == {
        "a": "#000000",
        "b": ["#000000", "#FFFFFF"],
    }
