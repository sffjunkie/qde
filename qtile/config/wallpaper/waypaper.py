import configparser
from pathlib import Path

from ..fs import user_config_dir
from .typedef import Wallpaper


"""
wallpaper = image.png
monitors = All

wallpaper = image1.png,image2.png
monitors = All, HDMI-A-1
"""


def get_wallpaper_waypaper(filepath: Path | None = None) -> list[Wallpaper]:
    if filepath is not None and filepath.is_absolute():
        waypaper_path = filepath
    else:
        if filepath is None:
            filepath = Path("config.ini")

        waypaper_path = user_config_dir("waypaper") / filepath

    parser = configparser.ConfigParser()
    with waypaper_path.open() as fp:
        parser.read_file(fp)

    wallpaper = parser["Settings"].get("wallpaper", None)
    monitor = parser["Settings"].get("monitors", "*")
    mode = parser["Settings"].get("fill", "fill")

    if wallpaper is None:
        return []

    if "," in wallpaper:
        images = wallpaper.split(",")
    else:
        images = [wallpaper]

    if "," in monitor:
        monitors = monitor.split(",")
    else:
        monitors = [monitor]

    assert len(images) == len(monitors)

    wallpapers = []
    for idx, image in enumerate(images):
        monitor = monitors[idx]
        if monitor == "All":
            monitor = "*"
        wallpapers.append(
            Wallpaper(
                image=image,
                monitor=monitor,
                mode=mode,
            )
        )

    return wallpapers
