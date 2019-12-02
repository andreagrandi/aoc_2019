from ..aoc.aoc_02 import run_codes


def test_run_codes():
    output, final_state = run_codes([1, 0, 0, 0, 99])
    assert output == 2
    assert final_state == [2, 0, 0, 0, 99]

    output, final_state = run_codes([2, 3, 0, 3, 99])
    assert output == 2
    assert final_state == [2, 3, 0, 6, 99]

    output, final_state = run_codes([2, 4, 4, 5, 99, 0])
    assert output == 2
    assert final_state == [2, 4, 4, 5, 99, 9801]

    output, final_state = run_codes([1, 1, 1, 4, 99, 5, 6, 0, 99])
    assert output == 30
    assert final_state == [30, 1, 1, 4, 2, 5, 6, 0, 99]
