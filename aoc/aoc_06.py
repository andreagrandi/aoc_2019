def get_total_direct_orbits(orbits_map):
    n_orbits = 0

    for orbit in orbits_map:
        next = orbits_map.get(orbit)

        while next is not None:
            n_orbits += 1
            next = orbits_map.get(next)
    return n_orbits


def get_nodes(orbits_map, node):
    nodes = []
    next = orbits_map.get(node)

    while next is not None:
        nodes.append(next)
        next = orbits_map.get(next)
    return nodes


def get_orbital_transfers(orbits_map, node_a, node_b):
    nodes_a = get_nodes(orbits_map, node_a)
    nodes_b = get_nodes(orbits_map, node_b)

    i = 0
    for n_a in nodes_a:
        k = 0
        for n_b in nodes_b:
            if n_a == n_b:
                print('They meet in: {0}'.format(n_a))
                return i + k
            k += 1
        i += 1
    return None


if __name__ == "__main__":
    with open('./aoc_06_input.txt', 'r') as file:
        orbits_map = {}

        for line in file:
            line = line.replace('\n', '')
            orbits = line.split(')')
            orbits_map[orbits[1]] = orbits[0]

        n_orbits = get_total_direct_orbits(orbits_map)
        n_transfers = get_orbital_transfers(orbits_map, 'YOU', 'SAN')
        print('Total number of direct orbits: {0}'.format(n_orbits))
        print('Minumum number of orbital transfers: {0}'.format(n_transfers))
