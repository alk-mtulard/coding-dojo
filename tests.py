#!/usr/bin/env python3
from unittest import TestCase, main

from rover import Direction, Position, Rover


class RoverInitalisationTests(TestCase):
    def test_it_should_face_the_given_initial_direction(self):
        initial_direction = Direction.NORTH

        rover = Rover(position=Position(x=1, y=1), direction=initial_direction)

        self.assertEqual(rover.direction, initial_direction)

    def test_it_should_be_at_the_given_initial_position(self):
        position = Position(x=2, y=2)

        rover = Rover(position=position, direction=Direction.NORTH)

        self.assertEqual(rover.position, position)


class RoverRotateRightTests(TestCase):
    def test_it_faces_east_when_it_was_facing_north(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.NORTH)

        rover.execute(["r"])

        self.assertEqual(rover.direction, Direction.EAST)

    def test_it_faces_south_when_it_was_facing_east(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.EAST)

        rover.execute(["r"])

        self.assertEqual(rover.direction, Direction.SOUTH)

    def test_it_faces_west_when_it_was_facing_south(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.SOUTH)

        rover.execute(["r"])

        self.assertEqual(rover.direction, Direction.WEST)

    def test_it_faces_north_when_it_was_facing_west(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.WEST)

        rover.execute(["r"])

        self.assertEqual(rover.direction, Direction.NORTH)


class RoverRotateLeftTests(TestCase):
    def test_it_faces_west_when_it_was_facing_north(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.NORTH)

        rover.execute(["l"])

        self.assertEqual(rover.direction, Direction.WEST)

    def test_it_faces_south_when_it_was_facing_west(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.WEST)

        rover.execute(["l"])

        self.assertEqual(rover.direction, Direction.SOUTH)

    def test_it_faces_east_when_it_was_facing_south(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.SOUTH)

        rover.execute(["l"])

        self.assertEqual(rover.direction, Direction.EAST)

    def test_it_faces_north_when_it_was_facing_east(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.EAST)

        rover.execute(["l"])

        self.assertEqual(rover.direction, Direction.NORTH)


class RoverForwardTests(TestCase):
    def test_it_increments_y_when_facing_north(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.NORTH)

        rover.execute("f")

        self.assertEqual(rover.position, Position(x=1, y=2))

    def test_it_increments_x_when_facing_east(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.EAST)

        rover.execute("f")

        self.assertEqual(rover.position, Position(x=2, y=1))

    def test_it_decrements_y_when_facing_south(self):
        rover = Rover(position=Position(x=5, y=5), direction=Direction.SOUTH)

        rover.execute("f")

        self.assertEqual(rover.position, Position(x=5, y=4))

    def test_it_decrements_x_when_facing_west(self):
        rover = Rover(position=Position(x=5, y=5), direction=Direction.WEST)

        rover.execute("f")

        self.assertEqual(rover.position, Position(x=4, y=5))

    def test_it_wraps_y_when_at_the_north_edge(self):
        rover = Rover(position=Position(x=5, y=5), direction=Direction.NORTH)

        rover.execute("f")

        self.assertEqual(rover.position, Position(x=5, y=1))

    def test_it_wraps_x_when_at_the_est_edge(self):
        rover = Rover(position=Position(x=5, y=5), direction=Direction.EAST)

        rover.execute("f")

        self.assertEqual(rover.position, Position(x=1, y=5))


class RoverBackwardTests(TestCase):
    def test_it_decrements_y_when_facing_north(self):
        rover = Rover(position=Position(x=5, y=5), direction=Direction.NORTH)

        rover.execute("b")

        self.assertEqual(rover.position, Position(x=5, y=4))

    def test_it_decrements_x_when_facing_east(self):
        rover = Rover(position=Position(x=5, y=5), direction=Direction.EAST)

        rover.execute("b")

        self.assertEqual(rover.position, Position(x=4, y=5))

    def test_it_increments_y_when_facing_south(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.SOUTH)

        rover.execute("b")

        self.assertEqual(rover.position, Position(x=1, y=2))

    def test_it_increments_x_when_facing_west(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.WEST)

        rover.execute("b")

        self.assertEqual(rover.position, Position(x=2, y=1))

    def test_it_wraps_y_when_at_the_south_edge(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.NORTH)

        rover.execute("b")

        self.assertEqual(rover.position, Position(x=1, y=5))

    def test_it_wraps_x_when_at_the_west_edge(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.EAST)

        rover.execute("b")

        self.assertEqual(rover.position, Position(x=5, y=1))


class RoverMultipleTests(TestCase):
    def test_it_should_accept_multiple_commands(self):
        rover = Rover(position=Position(x=1, y=1), direction=Direction.NORTH)

        rover.execute("ff")

        self.assertEqual(rover.position, Position(x=1, y=3))


if __name__ == "__main__":
    main()
