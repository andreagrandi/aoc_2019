import itertools
import os


def run_codes(codes, interactive_mode=False, inputs=[], index=0):
    while index <= len(codes):
        op = str(codes[index])

        if op.endswith('1'):
            op = op.zfill(4)

            if op[1] == '0':
                add_1 = codes[codes[index + 1]]
            elif op[1] == '1':
                add_1 = codes[index + 1]

            if op[0] == '0':
                add_2 = codes[codes[index + 2]]
            elif op[0] == '1':
                add_2 = codes[index + 2]

            codes[codes[index + 3]] = (add_1 + add_2)
            index += 4
        elif op.endswith('2'):
            op = op.zfill(4)

            if op[1] == '0':
                mul_1 = codes[codes[index + 1]]
            elif op[1] == '1':
                mul_1 = codes[index + 1]

            if op[0] == '0':
                mul_2 = codes[codes[index + 2]]
            elif op[0] == '1':
                mul_2 = codes[index + 2]

            codes[codes[index + 3]] = (mul_1 * mul_2)
            index += 4
        elif op.endswith('3'):
            address = int(codes[index + 1])

            if interactive_mode:
                number = int(input('Enter a number: '))
            else:
                number = int(inputs.pop(0))

            codes[address] = number
            index += 2
        elif op.endswith('4'):
            address = int(codes[index + 1])
            number = codes[address]

            if interactive_mode:
                print('The number at address {0} is {1}'.format(
                    address, number))
            else:
                return int(number), True, index + 2

            index += 2
        elif op.endswith('5'):
            op = op.zfill(4)

            if op[1] == '0':
                p1 = codes[codes[index + 1]]
            elif op[1] == '1':
                p1 = codes[index + 1]

            if op[0] == '0':
                p2 = codes[codes[index + 2]]
            elif op[0] == '1':
                p2 = codes[index + 2]

            if p1 != 0:
                index = p2
            else:
                index += 3
        elif op.endswith('6'):
            op = op.zfill(4)

            if op[1] == '0':
                p1 = codes[codes[index + 1]]
            elif op[1] == '1':
                p1 = codes[index + 1]

            if op[0] == '0':
                p2 = codes[codes[index + 2]]
            elif op[0] == '1':
                p2 = codes[index + 2]

            if p1 == 0:
                index = p2
            else:
                index += 3
        elif op.endswith('7'):
            op = op.zfill(4)

            if op[1] == '0':
                p1 = codes[codes[index + 1]]
            elif op[1] == '1':
                p1 = codes[index + 1]

            if op[0] == '0':
                p2 = codes[codes[index + 2]]
            elif op[0] == '1':
                p2 = codes[index + 2]

            if p1 < p2:
                codes[codes[index + 3]] = 1
            else:
                codes[codes[index + 3]] = 0

            index += 4
        elif op.endswith('8'):
            op = op.zfill(4)

            if op[1] == '0':
                p1 = codes[codes[index + 1]]
            elif op[1] == '1':
                p1 = codes[index + 1]

            if op[0] == '0':
                p2 = codes[codes[index + 2]]
            elif op[0] == '1':
                p2 = codes[index + 2]

            if p1 == p2:
                codes[codes[index + 3]] = 1
            else:
                codes[codes[index + 3]] = 0

            index += 4
        elif op.endswith('99'):
            return None, False, index


def run_amp(codes, setting, input_signal, index=0):
    if setting is not None and input_signal is not None:
        return run_codes(
            codes, interactive_mode=False, inputs=[setting, input_signal])

    if setting:
        return run_codes(
            codes, interactive_mode=False, inputs=[setting], index=index)
    else:
        return run_codes(
            codes, interactive_mode=False, inputs=[input_signal], index=index)


def find_highest_signal(codes, settings='', configuration={}):
    output_signals = []

    for phase_settings in itertools.permutations(settings):
        next = 0
        output = 0
        while next is not None:
            new_codes = [x for x in codes]
            output, _, _ = run_amp(new_codes, phase_settings[next], output)
            next = configuration.get(next)
        output_signals.append(output)
    return max(output_signals)


def find_highest_signal_loop(codes, settings='', configuration={}):
    output_signals = []

    for phase_settings in itertools.permutations(settings):
        phase_settings = list(phase_settings)
        next = 0
        output = 0
        is_running = True
        amp_codes = []
        final_output = 0

        amps_index = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0
        }

        for i in range(5):
            amp_codes.append([x for x in codes])

        while (next is not None) and is_running:
            setting = phase_settings[next]

            if setting:
                output, is_running, index = run_amp(
                    amp_codes[next], setting, output, amps_index[next])
                phase_settings[next] = None
            else:
                output, is_running, index = run_amp(
                    amp_codes[next], None, output, amps_index[next])

            amps_index[next] = index

            # I check if the code returned an output and we are on AMP E
            if output and next == 4:
                final_output = output

            next = configuration.get(next)
        output_signals.append(final_output)
    return max(output_signals)


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(current_dir + '/inputs/aoc_07_input.txt', 'r') as file:
        data = file.read().replace('\n', '')
        codes = data.split(',')
        codes = [int(i) for i in codes]

        configuration = {
            0: 1,
            1: 2,
            2: 3,
            3: 4
        }

        signal = find_highest_signal(
            codes, settings='01234', configuration=configuration)
        print('The highest signal is: {0}'.format(signal))

        configuration = {
            0: 1,
            1: 2,
            2: 3,
            3: 4,
            4: 0
        }

        signal = find_highest_signal_loop(
            codes, settings='56789', configuration=configuration)
        print('The highest signal loop is: {0}'.format(signal))
