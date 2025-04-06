from .typedef import (
    Margins,
    ScreenFraction,
    WindowLocation,
    WindowPosition,
)


def to_margins(margin: ScreenFraction | Margins = 0.0) -> Margins:
    if isinstance(margin, float):
        return Margins(margin, margin, margin, margin)
    elif isinstance(margin, Margins):
        return margin
    else:
        return Margins(0.1, 0.1, 0.1, 0.1)


def anchor_window(
    location: WindowLocation,
    width: ScreenFraction,
    height: ScreenFraction,
    margin: ScreenFraction | Margins = 0.0,
) -> WindowPosition:
    margins = to_margins(margin)
    w_width = min(width, 1.0 - (margins.left + margins.right))
    w_height = min(height, 1.0 - (margins.top + margins.bottom))

    if location == WindowLocation.Left:
        return WindowPosition(
            x=0.0 + margins.left,
            y=(1.0 - w_height) / 2.0,
            width=w_width,
            height=w_height,
        )
    elif location == WindowLocation.Right:
        return WindowPosition(
            x=1.0 - (w_width + margins.right),
            y=(1.0 - w_height) / 2.0,
            width=w_width,
            height=w_height,
        )
    elif location == WindowLocation.Top:
        return WindowPosition(
            x=(1.0 - w_width) / 2.0,
            y=0.0 + margins.top,
            width=w_width,
            height=w_height,
        )
    elif location == WindowLocation.Bottom:
        return WindowPosition(
            x=(1.0 - w_width) / 2.0,
            y=1.0 - (w_height + margins.bottom),
            width=w_width,
            height=w_height,
        )
    elif location == WindowLocation.TopLeft:
        return WindowPosition(
            x=0.0 + margins.left,
            y=0.0 + margins.top,
            width=w_width,
            height=w_height,
        )
    elif location == WindowLocation.TopCenter:
        return WindowPosition(
            x=(1.0 - w_width) / 2.0,
            y=0.0 + margins.top,
            width=w_width,
            height=w_height,
        )
    elif location == WindowLocation.TopRight:
        return WindowPosition(
            x=1.0 - w_width - margins.right,
            y=0.0 + margins.top,
            width=w_width,
            height=w_height,
        )
    elif location == WindowLocation.BottomLeft:
        return WindowPosition(
            x=0.0 + margins.left,
            y=1.0 - w_height - margins.bottom,
            width=w_width,
            height=w_height,
        )
    elif location == WindowLocation.BottomCenter:
        return WindowPosition(
            x=(1.0 - w_width) / 2.0,
            y=1.0 - w_height - margins.bottom,
            width=w_width,
            height=w_height,
        )
    elif location == WindowLocation.BottomRight:
        return WindowPosition(
            x=1.0 - w_width - margins.right,
            y=1.0 - w_height - margins.bottom,
            width=w_width,
            height=w_height,
        )
    elif location == WindowLocation.Centered:
        return WindowPosition(
            x=(1.0 - w_width) / 2.0,
            y=(1.0 - w_height) / 2.0,
            width=w_width,
            height=w_height,
        )
