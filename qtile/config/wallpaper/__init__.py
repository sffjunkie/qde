from .typedef import Wallpaper
from .waypaper import get_wallpaper_waypaper


def get_wallpaper() -> Wallpaper:
    wallpapers = get_wallpaper_waypaper()
    return wallpapers[0]
