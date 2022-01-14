from enum import Enum
from typing import Any, List, NamedTuple


class Delta(NamedTuple):
    dx: int
    dy: int


class Direction(Enum):
    NORTH = Delta(dx=0, dy=+1)
    SOUTH = Delta(dx=0, dy=-1)
    EAST = Delta(dx=+1, dy=0)
    WEST = Delta(dx=-1, dy=0)

    def right(self) -> "Direction":
        if self == Direction.NORTH:
            direction = Direction.EAST
        elif self == Direction.SOUTH:
            direction = Direction.WEST
        elif self == Direction.WEST:
            direction = Direction.NORTH
        elif self == Direction.EAST:
            direction = Direction.SOUTH
        return direction

    def left(self) -> "Direction":
        if self == Direction.WEST:
            direction = Direction.SOUTH
        elif self == Direction.SOUTH:
            direction = Direction.EAST
        elif self == Direction.EAST:
            direction = Direction.NORTH
        elif self == Direction.NORTH:
            direction = Direction.WEST
        return direction


class Position(NamedTuple):
    x: int
    y: int

    def __add__(self, delta: Any) -> "Position":
        if not isinstance(delta, Delta):
            raise ValueError
        return Position(
            x=self.x + delta.dx,
            y=self.y + delta.dy,
        )

    def __sub__(self, delta: Any) -> "Position":
        if not isinstance(delta, Delta):
            raise ValueError
        return Position(
            x=self.x - delta.dx,
            y=self.y - delta.dy,
        )


class Rover:
    def __init__(self, position: Position, direction: Direction) -> None:
        self._position = position
        self._direction = direction

    @property
    def direction(self) -> Direction:
        return self._direction

    @property
    def position(self) -> Position:
        return self._position

    def execute(self, commands: List[str]) -> None:
        if commands[0] == "r":
            self._direction = self._direction.right()
        elif commands[0] == "l":
            self._direction = self._direction.left()
        elif commands[0] == "f":
            self._position = self._position + self._direction.value
        elif commands[0] == "b":
            self._position = self._position - self._direction.value
