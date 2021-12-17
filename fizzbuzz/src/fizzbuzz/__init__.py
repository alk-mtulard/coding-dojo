__version__ = "0.1.0"

import sys


def get_result(input: int) -> str:
    is_multiple_of_3 = input % 3 == 0
    is_multiple_of_5 = input % 5 == 0

    if is_multiple_of_3 and is_multiple_of_5:
        return "FizzBuzz"

    if is_multiple_of_3:
        return "Fizz"

    if is_multiple_of_5:
        return "Buzz"

    return str(input)


def print_fizzbuzz_for_1_to_100(output=sys.stdout):
    for i in range(1, 101):
        line = get_result(i) + "\n"
        output.write(line)
