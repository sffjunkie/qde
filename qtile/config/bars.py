"""Bars for Qtile"""

import os

from libqtile.log_utils import logger  # type: ignore
from libqtile.bar import Bar as QBar  # type: ignore
from qtile_extras.widget import Spacer as QSpacer  # type: ignore

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
from .setting.model import Settings
from .theme.model import Theme
from .theme.iter import widget_color_iter


def build_top_bar(settings: Settings, theme: Theme) -> QBar | None:
    named_colors = theme.color.named
    _color_iter = widget_color_iter(theme)
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
    fg, bg = next(_color_iter)
    user_menu = UserMenu(
        ModuleContext(
            bar_context,
            settings,
            theme,
            props={
                "color": fg,
                "background": bg,
            },
        )
    )

    group_box = GroupBox(
        ModuleContext(
            bar_context,
            settings,
            theme,
            props={
                "background": named_colors.panel_bg,
            },
        )
    )

    current_layout = CurrentLayout(
        ModuleContext(
            bar_context,
            settings,
            theme,
            props={
                "background": named_colors.panel_bg,
            },
        )
    )

    start: list[WidgetModule] = [
        user_menu,
        group_box,
        current_layout,
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
                    "background": named_colors.panel_bg,
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
    fg, bg = next(_color_iter)
    weather_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "color": fg,
            "background": bg,
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

    fg, bg = next(_color_iter)
    date_time_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "color": fg,
            "background": bg,
        },
    )

    fg, bg = next(_color_iter)
    system_menu_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "color": fg,
            "background": bg,
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
    _color_iter = widget_color_iter(theme)

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

    if (net_dev := getattr(settings.device, "net", None)) is not None:
        fg, bg = next(_color_iter)
        network_status_context = ModuleContext(
            bar_context,
            settings,
            theme,
            props={
                "network": {
                    "interface": net_dev,
                },
                "color": fg,
                "background": bg,
            },
        )
        start.append(NetworkStatus(network_status_context))

    fg, bg = next(_color_iter)
    memory_status_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "memory": {
                "format": "{MemUsed:6.0f}M/{MemTotal:.0f}M",
            },
            "color": fg,
            "background": bg,
        },
    )
    start.append(MemoryStatus(memory_status_context))

    fg, bg = next(_color_iter)
    cpu_usage_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "color": fg,
            "background": bg,
        },
    )
    start.append(CPUUsageStatus(cpu_usage_context))

    fg, bg = next(_color_iter)
    cpu_temp_context = ModuleContext(
        bar_context,
        settings,
        theme,
        props={
            "color": fg,
            "background": bg,
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

    if settings.controller is not None:
        if settings.controller.music is not None:
            fg, bg = next(_color_iter)
            music_status_context = ModuleContext(
                bar_context,
                settings,
                theme,
                props={
                    "music": {
                        "status_format": "{play_status} {title} | {artist} | {album}",
                        "idle_format": "Play queue empty",
                    },
                    "color": fg,
                    "background": bg,
                },
            )
            end.append(MusicStatus(music_status_context))

        if settings.controller.volume is not None:
            fg, bg = next(_color_iter)
            volume_context = ModuleContext(
                bar_context,
                settings,
                theme,
                props={
                    "volume": {
                        "volume_up_command": settings.controller.volume.up,
                        "volume_down_command": settings.controller.volume.down,
                        "mute_command": settings.controller.volume.toggle,
                        "volume_app": settings.app.volume,
                    },
                    "color": fg,
                    "background": bg,
                },
            )
            end.append(VolumeStatus(volume_context))
    else:
        logger.warning(
            "No controller definitions, not craeting music and volume control widgets"
        )

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
