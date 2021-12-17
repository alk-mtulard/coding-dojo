import sys
from io import StringIO

from fizzbuzz import __version__, get_result, print_fizzbuzz_for_1_to_100


def test_version():
    assert __version__ == "0.1.0"


def test_when_multiple_of_3_return_fizz():
    result = get_result(3)

    assert result == "Fizz"


def test_when_multiple_of_5_return_buzz():
    result = get_result(5)

    assert result == "Buzz"


def test_when_not_multiple_3_or_5_return_number():
    result = get_result(1)

    assert result == "1"


def test_when_multiple_of_3_and_5_return_fizzbuzz():
    result = get_result(15)

    assert result == "FizzBuzz"


def test_print_1_to_100():
    output = StringIO()

    print_fizzbuzz_for_1_to_100(output)

    expected = "\n".join([get_result(i) for i in range(1, 101)]) + "\n"
    assert output.getvalue() == expected
