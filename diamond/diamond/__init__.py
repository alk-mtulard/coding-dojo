__version__ = "0.1.0"


import string


def get_diamond_border(input_letter):
    border = ""

    for letter in string.ascii_uppercase:
        border += letter
        if letter == input_letter:
            break

    return border


def get_diamond(input_letter):
    diamond = ""

    border = get_diamond_border(input_letter)
    nb_spaces = len(border) - 1

    lines = []

    for index, letter in enumerate(border):
        spaces_before = " " * (nb_spaces - index)

        if index == 0:
            line = spaces_before + letter
        else:
            spaces_between = " " * (2 * index - 1)
            line = spaces_before + letter + spaces_between + letter

        lines.append(line)

    lines.extend(lines[-2::-1])

    diamond = "\n".join(lines)

    return diamond
