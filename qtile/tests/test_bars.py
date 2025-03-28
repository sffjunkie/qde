from config.bars import build_top_bar


def test_bar_widget_bg(settings, theme):
    top = build_top_bar(settings, theme)

    assert top is not None
    assert len(top.widgets) > 0
