# The Elves quickly load you into a spacecraft and prepare to launch.

# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper.
# They haven't determined the amount of fuel required yet.

# Fuel required to launch a given module is based on its mass. Specifically,
# to find the fuel required for a module,
# take its mass, divide by three, round down, and subtract 2.

# For example:

#     For a mass of 12, divide by 3 and round down to get 4, then subtract 2
#     to get 2.
#     For a mass of 14, dividing by 3 and rounding down still yields 4, so the
#     fuel required is also 2.
#     For a mass of 1969, the fuel required is 654.
#     For a mass of 100756, the fuel required is 33583.

# The Fuel Counter-Upper needs to know the total fuel requirement.
# To find it, individually calculate the fuel needed for the mass of each
# module (your puzzle input),
# then add together all the fuel values.

import os


def get_required_fuel(mass):
    fuel = (mass // 3) - 2
    return fuel


if __name__ == "__main__":
    total_fuel = 0

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(current_dir + '/inputs/aoc_01_input.txt', 'r') as file:
        for line in file:
            mass = int(line)
            fuel = get_required_fuel(mass)
            total_fuel += fuel

    print('The required fuel is {0}'.format(total_fuel))
