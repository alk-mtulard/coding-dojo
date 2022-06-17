__version__ = "0.1.0"

from typing import List


def compress(uncompressed: List[int]) -> str:
    results = []
    while len(uncompressed) > 0:
        next_elem, uncompressed = get_next_elem(uncompressed)
        results.append(next_elem)
    return ",".join(results)


def get_next_elem(uncompressed: List[int]) -> str:

    if len(uncompressed) > 1:
        count = 1
        first_element = uncompressed[0]
        while len(uncompressed) > 1 and uncompressed[0] == uncompressed[1]:
            count += 1
            uncompressed = uncompressed[1:]
        if count != 1:
            uncompressed = uncompressed[1:]
            return (f"{first_element}*{count}", uncompressed)

    if len(uncompressed) > 2:
        first_element = uncompressed[0]
        while (
            len(uncompressed) > 2
            and uncompressed[2] - uncompressed[1] == uncompressed[1] - uncompressed[0]
        ):
            uncompressed = uncompressed[1:]
        if first_element != uncompressed[0]:
            last_element = uncompressed[1]
            step = abs(last_element - uncompressed[0])
            uncompressed = uncompressed[2:]

            if step == 1:
                return (f"{first_element}-{last_element}", uncompressed)
            else:
                return (f"{first_element}-{last_element}/{step}", uncompressed)

    return (str(uncompressed[0]), uncompressed[1:])
