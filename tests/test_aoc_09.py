from ..aoc.aoc_09 import IntCode


def test_intcode_read_existing_memory():
    codes = [1, 5, 9, 0, 21]
    ic = IntCode(codes)
    assert ic.read_memory(0) == 1
    assert ic.read_memory(1) == 5
    assert ic.read_memory(2) == 9
    assert ic.read_memory(3) == 0
    assert ic.read_memory(4) == 21


def test_intcode_read_outof_memory():
    codes = [1, 5, 9, 0, 21]
    ic = IntCode(codes)
    assert ic.read_memory(5) == 0


def test_intcode_get_parameter():
    codes = [1, 5, 9, 0, 21, 2, 3, 4, 2, 1, 0]
    ic = IntCode(codes, relative_base=2)
    assert ic.get_parameter(1, '0') == 2
    assert ic.get_parameter(1, '1') == 5
    assert ic.get_parameter(1, '2') == 4


def test_intcode_write_existing_memory():
    codes = [1, 5, 9, 0, 21]
    ic = IntCode(codes)
    ic.write_memory(0, 2)
    ic.write_memory(1, 10)
    assert ic.read_memory(0) == 2
    assert ic.read_memory(1) == 10


def test_intcode_write_outof_memory():
    codes = [1, 5, 9, 0, 21]
    ic = IntCode(codes)
    ic.write_memory(6, 8)
    ic.write_memory(10, 7)
    assert ic.read_memory(6) == 8
    assert ic.read_memory(10) == 7
    assert ic.read_memory(5) == 0
    assert len(ic.codes) == 11


def test_intcode_set_parameter():
    codes = [1, 5, 9, 0, 21, 2, 3, 4, 2, 1, 0]
    ic = IntCode(codes, relative_base=2)
    ic.set_parameter(1, '0', 4)
    ic.set_parameter(1, '2', 3)
    assert ic.read_memory(1) == 4
    assert ic.read_memory(3) == 3


def test_intcode_opcode_01():
    codes = [1001, 6, 1, 5, 99, 0, 6]
    ic = IntCode(codes)
    ic.run()
    assert ic.read_memory(5) == 7
    assert ic.codes == [1001, 6, 1, 5, 99, 7, 6]

    codes = [1101, 1, 1, 3, 99]
    ic = IntCode(codes)
    ic.run()
    assert ic.read_memory(3) == 2
    assert ic.codes == [1101, 1, 1, 2, 99]

    codes = [21101, 1, 1, 3, 99, 0]
    ic = IntCode(codes, relative_base=2)
    ic.run()
    assert ic.read_memory(5) == 2
    assert ic.codes == [21101, 1, 1, 3, 99, 2]

    codes = [1, 5, 6, 7, 99, 3, 5, 0]
    ic = IntCode(codes)
    ic.run()
    assert ic.read_memory(7) == 8
    assert ic.codes == [1, 5, 6, 7, 99, 3, 5, 8]

    codes = [101, 4, 5, 6, 99, 4, 0]
    ic = IntCode(codes)
    ic.run()
    assert ic.read_memory(6) == 8
    assert ic.codes == [101, 4, 5, 6, 99, 4, 8]


def test_intcode_opcode_02():
    codes = [1002, 6, 1, 5, 99, 0, 6]
    ic = IntCode(codes)
    ic.run()
    assert ic.read_memory(5) == 6
    assert ic.codes == [1002, 6, 1, 5, 99, 6, 6]

    codes = [1102, 1, 1, 3, 99]
    ic = IntCode(codes)
    ic.run()
    assert ic.read_memory(3) == 1
    assert ic.codes == [1102, 1, 1, 1, 99]

    codes = [21102, 1, 1, 3, 99, 0]
    ic = IntCode(codes, relative_base=2)
    ic.run()
    assert ic.read_memory(5) == 1
    assert ic.codes == [21102, 1, 1, 3, 99, 1]

    codes = [2, 5, 6, 7, 99, 3, 5, 0]
    ic = IntCode(codes)
    ic.run()
    assert ic.read_memory(7) == 15
    assert ic.codes == [2, 5, 6, 7, 99, 3, 5, 15]

    codes = [102, 4, 5, 6, 99, 4, 0]
    ic = IntCode(codes)
    ic.run()
    assert ic.read_memory(6) == 16
    assert ic.codes == [102, 4, 5, 6, 99, 4, 16]


def test_intcode_opcode_03():
    codes = [3, 3, 99, 0]
    inputs = [1]
    ic = IntCode(codes, inputs=inputs)
    ic.run()
    assert ic.read_memory(3) == 1
    assert ic.codes == [3, 3, 99, 1]

    codes = [203, 1, 99, 0]
    inputs = [1]
    ic = IntCode(codes, inputs=inputs, relative_base=2)
    ic.run()
    assert ic.read_memory(3) == 1
    assert ic.codes == [203, 1, 99, 1]


def test_intcode_opcode_04():
    codes = [4, 3, 99, 42]
    ic = IntCode(codes, interactive_mode=True)
    ic.run()
    assert 42 in ic.outputs

    codes = [104, 10, 99]
    ic = IntCode(codes, interactive_mode=True)
    ic.run()
    assert 10 in ic.outputs

    codes = [204, 1, 99, 42]
    ic = IntCode(codes, interactive_mode=True, relative_base=2)
    ic.run()
    assert 42 in ic.outputs


def test_intcode_opcode_05():
    codes = [5, 1, 4, 99, 6, 0, 99]
    ic = IntCode(codes)
    ic.run()
    assert ic.index == 6

    codes = [5, 4, 6, 99, 0, 0, 99]
    ic = IntCode(codes)
    ic.run()
    assert ic.index == 3

    codes = [1105, 1, 5, 0, 0, 99]
    ic = IntCode(codes)
    ic.run()
    assert ic.index == 5

    codes = [1105, 0, 5, 99, 0, 0]
    ic = IntCode(codes)
    ic.run()
    assert ic.index == 3

    codes = [2105, 1, 5, 0, 0, 0, 0, 8, 99]
    ic = IntCode(codes, relative_base=2)
    ic.run()
    assert ic.index == 8


def test_intcode_opcode_06():
    codes = [6, 5, 4, 99, 6, 0, 99]
    ic = IntCode(codes)
    ic.run()
    assert ic.index == 6

    codes = [6, 2, 6, 99, 0, 0, 99]
    ic = IntCode(codes)
    ic.run()
    assert ic.index == 3

    codes = [1106, 0, 5, 0, 0, 99]
    ic = IntCode(codes)
    ic.run()
    assert ic.index == 5

    codes = [1106, 1, 5, 99, 0, 0]
    ic = IntCode(codes)
    ic.run()
    assert ic.index == 3

    codes = [2106, 0, 5, 0, 0, 0, 0, 8, 99]
    ic = IntCode(codes, relative_base=2)
    ic.run()
    assert ic.index == 8


def test_intcode_opcode_07():
    codes = [7, 5, 6, 7, 99, 0, 1, 5]
    ic = IntCode(codes)
    ic.run()
    assert ic.codes[7] == 1
    assert ic.index == 4

    codes = [7, 5, 6, 7, 99, 1, 0, 5]
    ic = IntCode(codes)
    ic.run()
    assert ic.codes[7] == 0
    assert ic.index == 4

    codes = [1107, 0, 1, 5, 99, 0]
    ic = IntCode(codes)
    ic.run()
    assert ic.codes[5] == 1
    assert ic.index == 4

    codes = [1107, 1, 0, 5, 99, 1]
    ic = IntCode(codes)
    ic.run()
    assert ic.codes[5] == 0
    assert ic.index == 4

    codes = [2107, 0, 1, 5, 99, 0, 4]
    ic = IntCode(codes, relative_base=5)
    ic.run()
    assert ic.codes[5] == 1
    assert ic.index == 4

    codes = [2107, 8, 1, 5, 99, 1, 4]
    ic = IntCode(codes, relative_base=5)
    ic.run()
    assert ic.codes[5] == 0
    assert ic.index == 4


def test_intcode_opcode_08():
    codes = [8, 5, 6, 7, 99, 1, 1, 5]
    ic = IntCode(codes)
    ic.run()
    assert ic.codes[7] == 1
    assert ic.index == 4

    codes = [8, 5, 6, 7, 99, 1, 0, 5]
    ic = IntCode(codes)
    ic.run()
    assert ic.codes[7] == 0
    assert ic.index == 4

    codes = [1108, 3, 3, 5, 99, 0]
    ic = IntCode(codes)
    ic.run()
    assert ic.codes[5] == 1
    assert ic.index == 4

    codes = [1108, 1, 0, 5, 99, 1]
    ic = IntCode(codes)
    ic.run()
    assert ic.codes[5] == 0
    assert ic.index == 4

    codes = [2108, 0, 1, 5, 99, 0, 0]
    ic = IntCode(codes, relative_base=5)
    ic.run()
    assert ic.codes[5] == 1
    assert ic.index == 4

    codes = [2108, 8, 1, 5, 99, 1, 0]
    ic = IntCode(codes, relative_base=5)
    ic.run()
    assert ic.codes[5] == 0
    assert ic.index == 4


def test_intcode_opcode_09():
    codes = [9, 3, 99, 5]
    ic = IntCode(codes)
    ic.run()
    assert ic.relative_base == 5
    assert ic.index == 2


def test_intcode_example_01():
    codes = [
        109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100,
        16, 101, 1006, 101, 0, 99]
    ic = IntCode(codes, interactive_mode=True)
    ic.run()
    assert ic.outputs == [
        109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100,
        16, 101, 1006, 101, 0, 99]


def test_intcode_example_02():
    codes = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    ic = IntCode(codes, interactive_mode=True)
    ic.run()
    assert ic.outputs == [1219070632396864]


def test_intcode_example_03():
    codes = [104, 1125899906842624, 99]
    ic = IntCode(codes, interactive_mode=True)
    ic.run()
    assert ic.outputs == [1125899906842624]
