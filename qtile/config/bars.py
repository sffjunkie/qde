"""Bars for Qtile"""

import os
from itertools import cycle
from typing import Iterator

from libqtile.bar import Bar as QBar  # type: ignore
from qtile_extras.widget import Spacer as QSpacer  # type: ignore

from .color import contrast_color
from .qbar.context import BarContext
from .qmodule.base import WidgetModule
from .qmodule.context import ModuleContext
from .qmodule.cpu_temp_status import CPUTempStatus
from .qmodule.cpu_usage_status import CPUUsageStatus
from .qmodule.current_layout import CurrentLayout
from .qmodule.date_time import DateTime
from .qmodule.group_box import GroupBox
from .qmodule.memory_status import MemoryStatus
from .qmodule.music_status import MusicStatus
from .qmodule.network_status import NetworkStatus
from .qmodule.separator import Separator
from .qmodule.system_menu import SystemMenu
from .qmodule.user_menu import UserMenu
from .qmodule.volume_status import VolumeStatus
from .qmodule.weather import Weather
from .qmodule.window_name import WindowName
from .setting.typedef import Settings
from .theme.typedef import Theme


def fg_cycle(iterable, fg_light: str, fg_dark: str) -> Iterator:
    saved = []
    for element in iterable:
        fg = contrast_color(element, fg_light, fg_dark)
        yield fg
        saved.append(fg)

    while saved:
        for element in saved:
            yield element


def powerline_fg_iter(theme: Theme) -> Iterator:
    return fg_cycle(
        theme["color"]["named"]["widget_bg"],
        theme["color"]["named"]["widget_fg_light"],
        theme["color"]["named"]["widget_fg_dark"],
    )


def widget_bg_iter(theme: Theme) -> Iterator:
    return cycle(theme["color"]["named"]["widget_bg"])


def build_top_bar(settings: Settings, theme: Theme) -> QBar | None:
    named_colors = theme["color"]["named"]

    bg_iter = widget_bg_iter(theme)
    _fg_iter = powerline_fg_iter(theme)

    bar_context = BarContext("top", settings, theme)

    widgets = []

    separator = Separator(
        ModuleContext(
            bar_context,
            settings,
            theme,
        )
    )

    # region start
    start: list[WidgetModule] = [
        UserMenu(
            ModuleContext(
                bar_context,
                settings,
                theme,
                props={
                    "background": next(bg_iter),
                },
            )
        ),
        GroupBox(
            ModuleContext(
                bar_context,
                settings,
                theme,
                props={
                    "background": named_colors["panel_bg"],
                },
            )
        ),
        CurrentLayout(
            ModuleContext(
                bar_context,
                settings,
                theme,
                props={
                    "background": named_colors["panel_bg"],
                },
            )
        ),
    ]

    module_idx = 0
    for module_idx, group in enumerate(start):
        if module_idx != 0:
            widgets.extend(separator.widgets())

        widgets.extend(group.widgets(group_id=module_idx))
    # endregion

    # region middle
    middle: list[WidgetModule] = [
        WindowName(
            ModuleContext(
                bar_context,
                settings,
                theme,
                props={
                    "group": 4,
                    "background": named_colors["panel_bg"],
                },
            )
        ),
    ]

    if middle == []:
        widgets.append(QSpacer(background="#00000000"))
    else:
        widgets.extend(separator.widgets())
        for module_idx, group in enumerate(middle, start=module_idx + 1):
            widgets.extend(group.widgets(group_id=module_idx))
        widgets.extend(separator.widgets())
    # endregion

    # region end
    weather_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "background": next(bg_iter),
            "weather": {
                "app_key": os.environ.get("OWM_API_KEY", ""),
                "coordinates": {
                    "latitude": os.environ.get("USER_LOCATION_LATITUDE", "51.5"),
                    "longitude": os.environ.get("USER_LOCATION_LONGITUDE", "-0.15"),
                },
                "format": "{main_temp}/{main_feels_like}°{units_temperature} {icon}",
            },
        },
    )

    date_time_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "background": next(bg_iter),
        },
    )

    system_menu_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "background": next(bg_iter),
        },
    )

    end: list[WidgetModule] = [
        Weather(weather_context),
        DateTime(date_time_context),
        SystemMenu(system_menu_context),
    ]

    group_id = module_idx + 1
    for module_idx, group in enumerate(end):
        widgets.extend(group.widgets(group_id=group_id + module_idx))
        if module_idx != len(end) - 1:
            widgets.extend(separator.widgets())

    # endregion

    return QBar(
        widgets,
        size=bar_context.height,
        margin=bar_context.margin,
        background="#00000088",
    )


def build_bottom_bar(settings: Settings, theme: Theme) -> QBar | None:
    bg_iter = widget_bg_iter(theme)

    bar_context = BarContext("bottom", settings, theme)

    widgets = []

    separator = Separator(
        ModuleContext(
            bar_context,
            settings,
            theme,
        )
    )

    # region start
    start: list[WidgetModule] = []

    if (net_dev := settings["device"].get("net", None)) is not None:
        network_status_context = ModuleContext(
            bar_context,
            settings,
            theme,
            props={
                "network": {
                    "interface": net_dev,
                },
                "background": next(bg_iter),
            },
        )
        start.append(NetworkStatus(network_status_context))

    memory_status_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "memory": {
                "format": "{MemUsed:6.0f}M/{MemTotal:.0f}M",
            },
            "background": next(bg_iter),
        },
    )
    start.append(MemoryStatus(memory_status_context))

    cpu_usage_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "background": next(bg_iter),
        },
    )
    start.append(CPUUsageStatus(cpu_usage_context))

    cpu_temp_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "background": next(bg_iter),
        },
    )
    start.append(CPUTempStatus(cpu_temp_context))

    module_idx = -1
    for module_idx, group in enumerate(start):
        if module_idx != 0:
            widgets.extend(separator.widgets())

        widgets.extend(group.widgets(group_id=module_idx))
    # endregion

    # region middle
    middle: list[WidgetModule] = []

    if middle == []:
        widgets.append(QSpacer(background="#00000000"))
    else:
        widgets.extend(separator.widgets())
        for module_idx, group in enumerate(middle, start=module_idx + 1):
            widgets.extend(group.widgets(group_id=module_idx))
        widgets.extend(separator.widgets())
    # endregion

    # region end
    end: list[WidgetModule] = []

    if settings["controller"]["music"] is not None:
        music_status_context = ModuleContext(
            bar_context,
            settings,
            theme,
            props={
                "music": {
                    "status_format": "{play_status} {title} | {artist} | {album}",
                    "idle_format": "Play queue empty",
                },
                "background": next(bg_iter),
            },
        )
        end.append(MusicStatus(music_status_context))

    if settings["controller"]["volume"] is not None:
        volume_context = ModuleContext(
            bar_context,
            settings,
            theme,
            props={
                "background": next(bg_iter),
                "volume": {
                    "volume_up_command": settings["controller"]["volume"]["up"],
                    "volume_down_command": settings["controller"]["volume"]["down"],
                    "mute_command": settings["controller"]["volume"]["toggle"],
                    "volume_app": settings["app"]["volume"],
                },
            },
        )
        end.append(VolumeStatus(volume_context))

    group_id = module_idx + 1
    for module_idx, group in enumerate(end):
        widgets.extend(group.widgets(group_id=group_id + module_idx))
        if module_idx != len(end) - 1:
            widgets.extend(separator.widgets())
    # endregion

    return QBar(
        widgets,
        size=bar_context.height,
        margin=bar_context.margin,
        background="#00000088",
    )


def build_left_bar(settings: Settings, theme: Theme) -> QBar | None:
    return None


def build_right_bar(settings: Settings, theme: Theme) -> QBar | None:
    return None


def build_bars(settings: Settings, theme: Theme) -> dict[str, QBar]:
    bars = {}
    bars["top"] = build_top_bar(settings, theme)
    bars["bottom"] = build_bottom_bar(settings, theme)
    bars["left"] = build_left_bar(settings, theme)
    bars["right"] = build_right_bar(settings, theme)
    return bars
