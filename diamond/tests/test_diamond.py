from diamond import __version__
from diamond import get_diamond_border
from diamond import get_diamond


def test_version():
    assert __version__ == "0.1.0"


def test_given_a_letter_the_result_is_a_diamond_border():
    letter = "C"
    result = get_diamond_border(letter)

    assert result == "ABC"


def test_given_a_letter_the_result_is_a_diamond():
    letter = "D"

    result = get_diamond(letter)

    assert result == "\n".join(
        [
            "   A",
            "  B B",
            " C   C",
            "D     D",
            " C   C",
            "  B B",
            "   A",
        ]
    )
