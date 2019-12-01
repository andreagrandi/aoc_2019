from ..aoc.aoc_01 import get_required_fuel


def test_get_required_fuel():
    assert get_required_fuel(12) == 2
    assert get_required_fuel(14) == 2
    assert get_required_fuel(1969) == 654
    assert get_required_fuel(100756) == 33583
