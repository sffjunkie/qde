from qtile.config.setting.input.model import InputConfiguration
from config.setting.input.loader import load_inputs


def test_load_inputs(inputs: InputConfiguration):
    inputs = load_inputs()

    keyboard = inputs.keyboard["1452:591:Keychron Keychron K1"]
    assert keyboard.kb_layout == "hyper_super"

    mouse = inputs.pointer["1133:45082:MX Anywhere 2S Mouse"]
    assert mouse.natural_scroll
