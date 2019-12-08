from ..aoc.aoc_08 import (
    get_fewest_zero_digits,
    get_layers,
    get_stacked_layer
)


def test_get_fewest_zero_digits():
    layers = {
        0: '123456',
        1: '789012'
    }

    layer = get_fewest_zero_digits(layers)
    assert layer == '123456'

    layers = {
        0: '120112',
        1: '111222',
        2: '100200'
    }

    layer = get_fewest_zero_digits(layers)
    assert layer == '111222'


def test_get_layers():
    layers = get_layers('123456789012', 2, 3)
    assert layers == {
        0: '123456',
        1: '789012'
    }

    layers = get_layers('120112111222100200', 2, 3)
    assert layers == {
        0: '120112',
        1: '111222',
        2: '100200'
    }


def test_get_stacked_layer():
    layers = {
        0: '0222',
        1: '1122',
        2: '2212',
        3: '0000'
    }

    assert get_stacked_layer(layers, 4) == '0110'
