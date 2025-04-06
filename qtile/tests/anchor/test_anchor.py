from pytest import approx

from config.anchor import anchor_window
from config.anchor.typedef import WindowLocation


def test_anchor_left_fits():
    pos = anchor_window(
        WindowLocation.Left,
        width=0.5,
        height=0.7,
        margin=0.1,
    )

    assert pos.x == approx(0.1)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.15)
    assert pos.height == approx(0.7)


def test_anchor_left_too_wide():
    pos = anchor_window(
        WindowLocation.Left,
        width=0.81,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.25)
    assert pos.height == approx(0.5)


def test_anchor_left_too_high():
    pos = anchor_window(
        WindowLocation.Left,
        width=0.5,
        height=0.8,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_right_fits():
    pos = anchor_window(
        WindowLocation.Right,
        width=0.8,
        height=0.7,
        margin=0.1,
    )

    assert pos.x == approx(0.1)
    assert pos.width == approx(0.8)
    assert pos.y == approx(0.15)
    assert pos.height == approx(0.7)


def test_anchor_right_too_wide():
    pos = anchor_window(
        WindowLocation.Right,
        width=0.81,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.25)
    assert pos.height == approx(0.5)


def test_anchor_right_too_high():
    pos = anchor_window(
        WindowLocation.Right,
        width=0.5,
        height=0.9,
        margin=0.2,
    )

    assert pos.x == approx(0.3)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_top_fits():
    pos = anchor_window(
        WindowLocation.Top,
        width=0.8,
        height=0.4,
        margin=0.1,
    )

    assert pos.x == approx(0.1)
    assert pos.width == approx(0.8)
    assert pos.y == approx(0.1)
    assert pos.height == approx(0.4)


def test_anchor_top_too_wide():
    pos = anchor_window(
        WindowLocation.Top,
        width=0.81,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.5)


def test_anchor_top_too_high():
    pos = anchor_window(
        WindowLocation.Top,
        width=0.5,
        height=0.81,
        margin=0.2,
    )

    assert pos.x == approx(0.25)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_bottom_fits():
    pos = anchor_window(
        WindowLocation.Bottom,
        width=0.6,
        height=0.4,
        margin=0.1,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.5)
    assert pos.height == approx(0.4)


def test_anchor_bottom_too_wide():
    pos = anchor_window(
        WindowLocation.Bottom,
        width=0.81,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.3)
    assert pos.height == approx(0.5)


def test_anchor_bottom_too_high():
    pos = anchor_window(
        WindowLocation.Bottom,
        width=0.5,
        height=0.81,
        margin=0.2,
    )

    assert pos.x == approx(0.25)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_top_left_fits():
    pos = anchor_window(
        WindowLocation.TopLeft,
        width=0.5,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.5)


def test_anchor_top_left_too_high():
    pos = anchor_window(
        WindowLocation.TopLeft,
        width=0.5,
        height=0.7,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_top_left_too_wide():
    pos = anchor_window(
        WindowLocation.TopLeft,
        width=0.7,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.5)


def test_anchor_top_center_fits():
    pos = anchor_window(
        WindowLocation.TopCenter,
        width=0.5,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.25)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.5)


def test_anchor_top_center_too_high():
    pos = anchor_window(
        WindowLocation.TopCenter,
        width=0.5,
        height=0.7,
        margin=0.2,
    )

    assert pos.x == approx(0.25)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_top_center_too_wide():
    pos = anchor_window(
        WindowLocation.TopCenter,
        width=0.7,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.5)


def test_anchor_top_right_fits():
    pos = anchor_window(
        WindowLocation.TopRight,
        width=0.5,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.3)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.5)


def test_anchor_top_right_too_high():
    pos = anchor_window(
        WindowLocation.TopRight,
        width=0.5,
        height=0.7,
        margin=0.2,
    )

    assert pos.x == approx(0.3)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_top_right_too_wide():
    pos = anchor_window(
        WindowLocation.TopRight,
        width=0.7,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.5)


def test_anchor_bottom_left_fits():
    pos = anchor_window(
        WindowLocation.BottomLeft,
        width=0.5,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.3)
    assert pos.height == approx(0.5)


def test_anchor_bottom_left_too_high():
    pos = anchor_window(
        WindowLocation.BottomLeft,
        width=0.5,
        height=0.7,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_bottom_left_too_wide():
    pos = anchor_window(
        WindowLocation.BottomLeft,
        width=0.7,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.3)
    assert pos.height == approx(0.5)


def test_anchor_bottom_center_fits():
    pos = anchor_window(
        WindowLocation.BottomCenter,
        width=0.5,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.25)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.3)
    assert pos.height == approx(0.5)


def test_anchor_bottom_center_too_high():
    pos = anchor_window(
        WindowLocation.BottomCenter,
        width=0.5,
        height=0.7,
        margin=0.2,
    )

    assert pos.x == approx(0.25)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_bottom_center_too_wide():
    pos = anchor_window(
        WindowLocation.BottomCenter,
        width=0.7,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.3)
    assert pos.height == approx(0.5)


def test_anchor_bottom_right_fits():
    pos = anchor_window(
        WindowLocation.BottomRight,
        width=0.5,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.3)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.3)
    assert pos.height == approx(0.5)


def test_anchor_bottom_right_too_high():
    pos = anchor_window(
        WindowLocation.BottomRight,
        width=0.5,
        height=0.7,
        margin=0.2,
    )

    assert pos.x == approx(0.3)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_bottom_right_too_wide():
    pos = anchor_window(
        WindowLocation.BottomRight,
        width=0.7,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.3)
    assert pos.height == approx(0.5)


def test_anchor_centered_fits():
    pos = anchor_window(
        WindowLocation.Centered,
        width=0.5,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.25)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.25)
    assert pos.height == approx(0.5)


def test_anchor_centered_too_high():
    pos = anchor_window(
        WindowLocation.Centered,
        width=0.5,
        height=0.7,
        margin=0.2,
    )

    assert pos.x == approx(0.25)
    assert pos.width == approx(0.5)
    assert pos.y == approx(0.2)
    assert pos.height == approx(0.6)


def test_anchor_centered_too_wide():
    pos = anchor_window(
        WindowLocation.Centered,
        width=0.9,
        height=0.5,
        margin=0.2,
    )

    assert pos.x == approx(0.2)
    assert pos.width == approx(0.6)
    assert pos.y == approx(0.25)
    assert pos.height == approx(0.5)
