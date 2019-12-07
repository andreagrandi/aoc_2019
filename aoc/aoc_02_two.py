import os
from aoc_02 import run_codes


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(current_dir + '/inputs/aoc_02_input.txt', 'r') as file:
        data = file.read().replace('\n', '')
        data = data.split(',')

        for noun in range(100):
            for verb in range(100):
                # Reinitialise memory
                codes = [int(i) for i in data]

                # Set noun and verb
                codes[1] = noun
                codes[2] = verb

                # Run the code
                output, final_state = run_codes(codes)

                if output == 19690720:
                    result = 100 * noun + verb
                    print('100 * noun + verb is: {0}'.format(result))
                    break
