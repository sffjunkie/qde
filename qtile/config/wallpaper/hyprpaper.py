from pathlib import Path

from ..fs import user_config_dir, read_ini
from .typedef import Wallpaper


def get_wallpaper_hyprpaper(filepath: Path | None = None) -> list[Wallpaper]:
    if filepath is not None and filepath.is_absolute():
        settings_path = filepath
    else:
        if filepath is None:
            filepath = Path("settings.yaml")

        settings_path = user_config_dir() / filepath

    try:
        data = read_ini(settings_path, has_sections=False)
        wallpaper_defs = data["wallpaper"]
        if not isinstance(wallpaper_defs, list):
            wallpaper_defs = [wallpaper_defs]

        wallpapers = []
        for wdef in wallpaper_defs:
            monitor, image = wdef.split(",", maxsplit=1)
            monitor = monitor.strip()
            image = image.strip()

            if monitor == "":
                monitor = "*"

            if ":" in image:
                mode, image = image.split(":", maxsplit=1)
            else:
                mode = "fill"

            wp = Wallpaper(
                image=image.strip(),
                mode=mode,
                monitor=monitor,
            )
            wallpapers.append(wp)

        return wallpapers
    except KeyError:
        return []
