from pathlib import Path

from config.wallpaper.waypaper import get_wallpaper_waypaper
from config.wallpaper.hyprpaper import get_wallpaper_hyprpaper


def test_waypaper():
    data_dir = Path(__file__).parent
    p = data_dir / "data" / "waypaper.ini"

    wallpaper = get_wallpaper_waypaper(p)

    assert len(wallpaper) == 1
    assert wallpaper[0].image == "~/pictures/wallpaper/dt-walpaper/0184.jpg"
    assert wallpaper[0].monitor == "*"
    assert wallpaper[0].mode == "tile"


def test_hyprpaper():
    data_dir = Path(__file__).parent
    p = data_dir / "data" / "hyprpaper.conf"

    wallpaper = get_wallpaper_hyprpaper(p)

    assert len(wallpaper) == 2
    assert wallpaper[0].image == "~/pictures/wallpaper/dt-walpaper/0001.jpg"
    assert wallpaper[0].monitor == "*"
    assert wallpaper[0].mode == "fill"
