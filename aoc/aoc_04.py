"""
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a
password. The Elves had written the password on a sticky note, but someone
threw it out.

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever
    increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input
meet these criteria?

--- Part Two ---

An Elf just remembered one more important detail: the two adjacent
matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule,
the following are now true:

    112233 meets these criteria because the digits never decrease and
    all repeated digits are exactly two digits long.
    123444 no longer meets the criteria (the repeated 44 is part of a
    larger group of 444).
    111122 meets the criteria (even though 1 is repeated more than twice,
    it still contains a double 22).

How many different passwords within the range given in your puzzle input
meet all of the criteria?

"""


def has_double_digits(number):
    double_digits = ['11', '22', '33', '44', '55', '66', '77', '88', '99']
    digits = str(number)

    for i in range(len(digits) - 1):
        if digits[i:i+2] in double_digits:
            if i == 0:
                if digits[i] != digits[i+2]:
                    return True
            elif 0 < i < len(digits) - 2:
                if digits[i] != digits[i+2] and digits[i] != digits[i-1]:
                    return True
            else:
                if digits[i] != digits[i-1]:
                    return True
    return False


def never_decrease_digits(number):
    digits = str(number)

    for i in range(len(digits) - 1):
        if int(digits[i+1]) < int(digits[i]):
            return False
    return True


if __name__ == "__main__":
    lower_number = 138241
    higher_number = 674034
    passwords = 0

    for n in range(lower_number, higher_number + 1):
        if has_double_digits(n) and never_decrease_digits(n):
            passwords += 1

    print('The number of valid passwords is: {0}'.format(passwords))
