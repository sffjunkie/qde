from config.anchor import to_margins
from config.anchor.typedef import Margins


def test_margin_float():
    m = to_margins(0.3)
    assert m.top == 0.3
    assert m.right == 0.3
    assert m.bottom == 0.3
    assert m.left == 0.3


def test_margins():
    m = Margins(0.1, 0.2, 0.3, 0.4)
    assert m.top == 0.1
    assert m.right == 0.2
    assert m.bottom == 0.3
    assert m.left == 0.4
