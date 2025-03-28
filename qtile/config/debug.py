import sys

from libqtile.log_utils import logger  # type: ignore
from libqtile import __path__ as libqtile_path  # type: ignore


def show_runtime_info() -> None:
    logger.warning(f"python prefix: {sys.prefix}")
    logger.warning(f"python version: {sys.version}")
    logger.warning(f"python platform: {sys.platform}")
    logger.warning(f"python path: {sys.path}")
    logger.warning(f"libqtile path: {libqtile_path}")
