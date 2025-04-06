import re
from libqtile.config import Match  # type: ignore
from libqtile.config import Group  # type: ignore

from ..setting.model import Settings

SUPERSCRIPT = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
SUBSCRIPT = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"]

DECORATION = "superscript"


def decoration(decoration: str | None, group_idx: int) -> str:
    if decoration == "superscript":
        return SUPERSCRIPT[group_idx]
    elif decoration == "subscript":
        return SUBSCRIPT[group_idx]
    else:
        return ""


def build_groups(settings: Settings) -> list[Group]:
    groups = []

    if settings.group is not None:
        for idx, group_def in enumerate(settings.group.groups, 1):
            matches = None
            if group_def.matches is not None:
                matches = build_match(group_def.matches)

            label = group_def.name + (
                decoration(settings.group.decoration, idx)
                if settings.group.decoration is not None
                else ""
            )

            group = Group(
                name=str(idx),
                label=label,
                matches=matches,
            )

            groups.append(group)

    return groups


def build_match(regexes: list[str]) -> list[Match]:
    return [Match(wm_class=re.compile(regex)) for regex in regexes]
