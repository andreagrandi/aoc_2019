def run_codes(codes):
    index = 0

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
            number = int(input('Enter a number: '))
            codes[address] = number
            index += 2
        elif op.endswith('4'):
            address = int(codes[index + 1])
            number = codes[address]
            print('The number at address {0} is {1}'.format(address, number))
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
            return codes[0], codes


if __name__ == "__main__":
    with open('./aoc_05_input.txt', 'r') as file:
        data = file.read().replace('\n', '')
        codes = data.split(',')
        codes = [int(i) for i in codes]
        run_codes(codes)
