from pathlib import Path

from config.wallpaper.hyprpaper import get_wallpaper_hyprpaper


def test_hyprpaper_settings():
    data_dir = Path(__file__).parent.parent
    p = data_dir / "data" / "hyprpaper.conf"

    wallpaper = get_wallpaper_hyprpaper(p)

    assert len(wallpaper) == 2
    assert wallpaper[0].image == "~/pictures/wallpaper/dt-walpaper/0001.jpg"
    assert wallpaper[0].monitor == "*"
    assert wallpaper[0].mode == "fill"
