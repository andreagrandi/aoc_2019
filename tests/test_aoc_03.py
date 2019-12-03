from ..aoc.aoc_03 import (
    get_steps, get_all_steps,
    get_manhattan_distance,
    compute_wires)


def test_get_steps():
    steps = get_steps((0, 0), 'R5')
    assert steps == [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]

    steps = get_steps((0, 0), 'L5')
    assert steps == [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0)]

    steps = get_steps((0, 0), 'U5')
    assert steps == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]

    steps = get_steps((0, 0), 'D5')
    assert steps == [(0, 0), (0, -1), (0, -2), (0, -3), (0, -4), (0, -5)]


def test_get_all_steps():
    moves = ['R3', 'U2', 'L1']
    steps = get_all_steps(moves)
    assert steps == [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(3, 0), (3, 1), (3, 2)],
        [(3, 2), (2, 2)]
    ]


def test_get_manhattan_distance():
    assert get_manhattan_distance((0, 0), (3, 3)) == 6


def test_compute_wires():
    moves_a = [
        'R75', 'D30', 'R83', 'U83', 'L12',
        'D49', 'R71', 'U7', 'L72']
    moves_b = [
        'U62', 'R66', 'U55', 'R34', 'D71',
        'R55', 'D58', 'R83']

    path_a = get_all_steps(moves_a)
    path_b = get_all_steps(moves_b)

    distance, n_steps = compute_wires(path_a, path_b)
    assert distance == 159
    assert n_steps == 610

    moves_a = [
        'R98', 'U47', 'R26', 'D63', 'R33', 'U87',
        'L62', 'D20', 'R33', 'U53', 'R51']
    moves_b = [
        'U98', 'R91', 'D20', 'R16', 'D67',
        'R40', 'U7', 'R15', 'U6', 'R7'
    ]

    path_a = get_all_steps(moves_a)
    path_b = get_all_steps(moves_b)

    distance, n_steps = compute_wires(path_a, path_b)
    assert distance == 135
    assert n_steps == 410
