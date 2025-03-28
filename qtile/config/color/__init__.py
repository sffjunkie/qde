import string

from .typedef import RGBColor, RGBHex, Opacity


def opacity_to_str(opacity: Opacity) -> str:
    return hex(int(opacity * 255.0))[2:]


def is_color(value: str) -> bool:
    return len(value) == 6 and all([ch in string.hexdigits for ch in value])


def is_base16(value: str) -> bool:
    return (
        len(value) == 6
        and value[:4] == "base"
        and value[4] in string.hexdigits
        and value[5] in string.hexdigits
    )


def rgb_intensity(rgb: RGBColor):
    """Convert an RGB color to its intensity"""

    return rgb[0] * 0.299 + rgb[1] * 0.587 + rgb[2] * 0.114


def contrast_color(
    color: RGBHex,
    light: RGBHex = "FFFFFF",
    dark: RGBHex = "000000",
) -> str:
    """Return either the light ior dark color
    whichever provides the most contrast"""

    rgb = rgbhex_to_rgb(color)
    if rgb is None:
        return light

    if rgb == (0.0, 0.0, 0.0) or rgb_intensity(rgb) < (160.0 / 255.0):
        return light

    return dark


def rgbhex_to_rgb(value: RGBHex, allow_short: bool = True) -> RGBColor | None:
    """Convert from a hex color string of the form `#abc` or `#abcdef` to an
    RGB tuple.

    :param value: The value to convert
    :type value: str
    :param allow_short: If True then the short of form of an hex value is
                        accepted e.g. #fff
    :type allow_short:  bool
    """
    if value[0] == "#":
        value = value[1:]

    for ch in value:
        if ch not in string.hexdigits:
            return None

    if len(value) == 6:
        # The following to_iterable function is based on the
        # :func:`grouper` function in the Python standard library docs
        # http://docs.python.org/library/itertools.html
        def to_iterable() -> RGBColor:
            # pylint: disable=missing-docstring
            args = [iter(value[1:])] * 2
            return RGBColor([int("%s%s" % t, 16) / 255 for t in zip(*args)])

    elif len(value) == 3 and allow_short:

        def to_iterable() -> RGBColor:
            # pylint: disable=missing-docstring
            return RGBColor([int("%s%s" % (t, t), 16) / 255 for t in value[1:]])

    else:
        return None

    try:
        return to_iterable()
    except ValueError:
        return None


def rgbcolor_to_rgb_hex(value: RGBColor) -> RGBHex:
    """Convert from an (R, G, B) tuple to a hex color.

    :param value: The RGB value to convert

    R, G and B should be in the range 0.0 - 1.0
    """
    color = "".join(["%02x" % x1 for x1 in [int(x * 255) for x in value]])
    return "#%s" % color
