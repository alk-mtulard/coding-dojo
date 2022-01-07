from mars_rover import Position, Rover, __version__


def test_version():
    assert __version__ == "0.1.0"


def test_forward_increments_x_position_when_facing_north():
    rover = Rover(Position(x=1, y=1), direction="N")

    rover.move(["f"])

    assert rover.position == Position(x=2, y=1)


def test_forward_decrements_y_position_when_facing_west():
    rover = Rover(Position(x=2, y=2), direction="W")

    rover.move(["f"])

    assert rover.position == Position(x=2, y=1)


def test_forward_decrements_x_position_when_facing_south():
    rover = Rover(Position(x=2, y=2), direction="S")

    rover.move(["f"])

    assert rover.position == Position(x=1, y=2)


def test_forward_increments_y_position_when_facing_est():
    rover = Rover(Position(x=2, y=2), direction="E")

    rover.move(["f"])

    assert rover.position == Position(x=2, y=3)


def test_backward_decrements_x_when_facing_north():
    rover = Rover(Position(x=2, y=2), direction="N")

    rover.move(["b"])

    assert rover.position == Position(x=1, y=2)


def test_backward_increments_x_when_facing_south():
    rover = Rover(Position(x=1, y=1), direction="S")

    rover.move(["b"])

    assert rover.position == Position(x=2, y=1)


def test_turn_left_changes_direction():
    rover = Rover(Position(x=1, y=1), direction="N")

    rover.move(["l"])

    assert rover.direction == "W"


def test_turn_right_changes_direction():
    rover = Rover(Position(x=1, y=1), direction="N")

    rover.move(["r"])

    assert rover.direction == "E"
