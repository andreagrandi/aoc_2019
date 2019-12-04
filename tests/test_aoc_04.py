from ..aoc.aoc_04 import has_double_digits, never_decrease_digits


def test_has_double_digits():
    assert has_double_digits(111111) is False
    assert has_double_digits(122345) is True
    assert has_double_digits(123344) is True
    assert has_double_digits(123456) is False
    assert has_double_digits(135789) is False
    assert has_double_digits(124689) is False


def test_has_increasing_digits():
    assert never_decrease_digits(111111) is True
    assert never_decrease_digits(112334) is True
    assert never_decrease_digits(123456) is True
    assert never_decrease_digits(123450) is False
    assert never_decrease_digits(123416) is False
    assert never_decrease_digits(912345) is False


def test_double_digits_not_larger_group():
    assert has_double_digits(112233) is True
    assert has_double_digits(123444) is False
    assert has_double_digits(111122) is True
