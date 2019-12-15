import os


class IntCode:

    def __init__(
            self, codes, interactive_mode=False, inputs=[], index=0,
            relative_base=0):
        self.codes = codes
        self.interactive_mode = interactive_mode
        self.inputs = inputs
        self.index = index
        self.relative_base = relative_base
        self.outputs = []

    def read_memory(self, address):
        if address < len(self.codes):
            return self.codes[address]
        else:
            zeros_extension_lenght = address - (len(self.codes) - 1)
            extension = [0 for x in range(zeros_extension_lenght)]
            self.codes.extend(extension)
            return self.codes[address]

    def write_memory(self, address, value):
        if address < len(self.codes):
            self.codes[address] = value
        else:
            zeros_extension_lenght = address - len(self.codes)
            extension = [0 for x in range(zeros_extension_lenght)]
            extension.append(value)
            self.codes.extend(extension)

    def get_parameter(self, address, mode):
        if mode == '0':
            address_to_read = self.read_memory(address)
            value = self.read_memory(address_to_read)
        elif mode == '1':
            value = self.read_memory(address)
        elif mode == '2':
            address_to_read = self.read_memory(address)
            value = self.read_memory(address_to_read + self.relative_base)

        return value

    def set_parameter(self, address, mode, value):
        if mode == '0':
            self.write_memory(address, value)
        elif mode == '2':
            self.write_memory(address + self.relative_base, value)

    def run(self):
        while self.index <= len(self.codes):
            op = str(self.codes[self.index]).zfill(5)

            if op.endswith('01'):
                p1 = self.get_parameter(self.index + 1, op[2])
                p2 = self.get_parameter(self.index + 2, op[1])
                self.set_parameter(
                    self.read_memory(self.index + 3), op[0], p1 + p2)
                self.index += 4
            elif op.endswith('02'):
                p1 = self.get_parameter(self.index + 1, op[2])
                p2 = self.get_parameter(self.index + 2, op[1])
                self.set_parameter(
                    self.read_memory(self.index + 3), op[0], p1 * p2)
                self.index += 4
            elif op.endswith('03'):
                address = self.read_memory(self.index + 1)

                if self.interactive_mode:
                    number = int(input('Enter a number: '))
                else:
                    number = int(self.inputs.pop(0))

                self.set_parameter(address, op[2], number)
                self.index += 2
            elif op.endswith('04'):
                number = self.get_parameter(self.index + 1, op[2])

                if self.interactive_mode:
                    self.outputs.append(number)
                    print(number)
                else:
                    return int(number), True, self.index + 2

                self.index += 2
            elif op.endswith('05'):
                p1 = self.get_parameter(self.index + 1, op[2])
                p2 = self.get_parameter(self.index + 2, op[1])

                if p1 != 0:
                    self.index = p2
                else:
                    self.index += 3
            elif op.endswith('06'):
                p1 = self.get_parameter(self.index + 1, op[2])
                p2 = self.get_parameter(self.index + 2, op[1])

                if p1 == 0:
                    self.index = p2
                else:
                    self.index += 3
            elif op.endswith('07'):
                p1 = self.get_parameter(self.index + 1, op[2])
                p2 = self.get_parameter(self.index + 2, op[1])

                if p1 < p2:
                    self.set_parameter(
                        self.read_memory(self.index + 3), op[0], 1)
                else:
                    self.set_parameter(
                        self.read_memory(self.index + 3), op[0], 0)

                self.index += 4
            elif op.endswith('08'):
                p1 = self.get_parameter(self.index + 1, op[2])
                p2 = self.get_parameter(self.index + 2, op[1])

                if p1 == p2:
                    self.set_parameter(
                        self.read_memory(self.index + 3), op[0], 1)
                else:
                    self.set_parameter(
                        self.read_memory(self.index + 3), op[0], 0)

                self.index += 4
            elif op.endswith('09'):
                p1 = self.get_parameter(self.index + 1, op[2])
                self.relative_base += p1
                self.index += 2
            elif op.endswith('99'):
                return None, False, self.index


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(current_dir + '/inputs/aoc_09_input.txt', 'r') as file:
        data = file.read().replace('\n', '')
        codes = data.split(',')
        codes = [int(i) for i in codes]
        ic = IntCode(codes, interactive_mode=True)
        ic.run()
