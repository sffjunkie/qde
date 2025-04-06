from pathlib import Path

from config.wallpaper.waypaper import get_wallpaper_waypaper


def test_waypaper_settings():
    data_dir = Path(__file__).parent.parent
    p = data_dir / "data" / "waypaper.ini"

    wallpaper = get_wallpaper_waypaper(p)

    assert len(wallpaper) == 1
    assert wallpaper[0].image == "~/pictures/wallpaper/dt-walpaper/0184.jpg"
    assert wallpaper[0].monitor == "*"
    assert wallpaper[0].mode == "tile"
