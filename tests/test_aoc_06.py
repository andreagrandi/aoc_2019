from ..aoc.aoc_06 import get_nodes, get_orbital_transfers


orbits_map = {
    'B': 'COM',
    'C': 'B',
    'D': 'C',
    'E': 'D',
    'F': 'E',
    'G': 'B',
    'H': 'G',
    'I': 'D',
    'J': 'E',
    'K': 'J',
    'L': 'K',
    'YOU': 'K',
    'SAN': 'I'
}


def test_get_nodes():
    nodes = get_nodes(orbits_map, 'YOU')
    assert nodes == ['K', 'J', 'E', 'D', 'C', 'B', 'COM']

    nodes = get_nodes(orbits_map, 'L')
    assert nodes == ['K', 'J', 'E', 'D', 'C', 'B', 'COM']

    nodes = get_nodes(orbits_map, 'F')
    assert nodes == ['E', 'D', 'C', 'B', 'COM']

    nodes = get_nodes(orbits_map, 'SAN')
    assert nodes == ['I', 'D', 'C', 'B', 'COM']

    nodes = get_nodes(orbits_map, 'C')
    assert nodes == ['B', 'COM']

    nodes = get_nodes(orbits_map, 'COM')
    assert nodes == []


def test_get_orbital_transfers():
    n_transfers = get_orbital_transfers(orbits_map, 'YOU', 'SAN')
    assert n_transfers == 4
