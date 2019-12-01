from ..aoc.aoc_01_two import get_required_fuel


def test_get_required_fuel():
    assert get_required_fuel(14) == 2
    assert get_required_fuel(1969) == 966
    assert get_required_fuel(100756) == 50346
