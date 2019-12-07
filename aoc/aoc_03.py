import os


def get_steps(point, move):
    """
    Given a Point coordinates and a move, it calculates the list of Points
    required to complete the move.
    """
    direction = move[0]
    steps = int(move[1:])

    if direction == 'R':
        return [
            (x, point[1]) for x in range(point[0], point[0] + steps + 1)]
    elif direction == 'L':
        return [
            (x, point[1]) for x in range(point[0], point[0] - steps - 1, -1)]
    elif direction == 'U':
        return [
            (point[0], y) for y in range(point[1], point[1] + steps + 1)]
    elif direction == 'D':
        return [
            (point[0], y) for y in range(point[1], point[1] - steps - 1, -1)]


def get_all_steps(moves):
    all_steps = []
    starting_point = (0, 0)

    for move in moves:
        steps = get_steps(starting_point, move)
        all_steps.append(steps)
        starting_point = steps[-1:][0]

    return all_steps


def get_manhattan_distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def compute_wires(path_a, path_b):
    distances = []
    total_steps = []
    n_steps_a = 0

    for steps_a in path_a:
        n_steps_b = 0
        for steps_b in path_b:
            in_common = list(set(steps_a).intersection(steps_b))
            if len(in_common) > 0:
                point = in_common[0]
                distance_a = get_manhattan_distance(steps_a[0], point)
                distance_b = get_manhattan_distance(steps_b[0], point)
                distance = get_manhattan_distance((0, 0), point)

                if distance > 0:
                    distances.append(distance)

                if distance_a > 0 and distance_b > 0:
                    total_steps.append(
                        n_steps_a + n_steps_b + distance_a + distance_b)

            n_steps_b += len(steps_b) - 1
        n_steps_a += len(steps_a) - 1

    return min(distances), min(total_steps)


if __name__ == "__main__":
    wires = []
    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(current_dir + '/inputs/aoc_03_input.txt', 'r') as file:
        for line in file:
            data = line.replace('\n', '').split(',')
            wires.append(data)

    moves_a = wires[0]
    moves_b = wires[1]

    path_a = get_all_steps(moves_a)
    path_b = get_all_steps(moves_b)

    distance, steps = compute_wires(path_a, path_b)

    print('The minimum crossing distance is: {0}'.format(distance))
    print('The minimum number of steps is: {0}'.format(steps))
