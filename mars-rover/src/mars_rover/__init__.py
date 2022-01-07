__version__ = "0.1.0"


from typing import List, NamedTuple


class Position(NamedTuple):
    x: int
    y: int


class Rover:
    def __init__(self, position: Position, direction: str) -> None:
        self._x = position[0]
        self._y = position[1]
        self._direction = direction

    @property
    def position(self) -> Position:
        return Position(self._x, self._y)

    @property
    def direction(self) -> str:
        return self._direction

    def move(self, commands: List[str]) -> None:
        for command in commands:
            if command == "f":
                self._forward()
            if command == "b":
                self._backward()
            if command == "l":
                self._direction = "W"
            if command == "r":
                self._direction = "E"

    def _forward(self):
        if self.direction == "N":
            self._x += 1
        if self.direction == "W":
            self._y -= 1
        if self.direction == "S":
            self._x -= 1
        if self.direction == "E":
            self._y += 1

    def _backward(self):
        if self.direction == "N":
            self._x -= 1
        if self.direction == "S":
            self._x += 1
