import re
from libqtile.config import Match  # type: ignore
from libqtile.config import Group  # type: ignore

from .setting.typedef import Settings

SUPERSCRIPT = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
SUBSCRIPT = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"]

DECORATION = "superscript"


def decoration(group_idx: int) -> str:
    if DECORATION == "superscript":
        return SUPERSCRIPT[group_idx]
    elif DECORATION == "subscript":
        return SUBSCRIPT[group_idx]
    else:
        return ""


def build_groups(settings: Settings) -> list[Group]:
    groups = []
    for idx, group_def in enumerate(settings["group"], 1):
        match_defs = group_def.get("matches", None)
        matches = None
        if match_defs:
            matches = build_match(match_defs)

        group = Group(
            name=str(idx),
            label=group_def["name"] + decoration(idx),
            matches=matches,
        )

        groups.append(group)
    return groups


def build_match(regexes: list[str]) -> list[Match]:
    return [Match(wm_class=re.compile(regex)) for regex in regexes]
