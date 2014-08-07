from herbert import interpreter


def walk(world, code):
    code, _, _ = interpreter.walk_world(world, code)
    return code


def walk_position(world, code):
    code, poistion, _ = interpreter.walk_world(world, code)
    return code, poistion


def walk_position_solved(world, code):
    return interpreter.walk_world(world, code)


def test_starting_point():
    world = """
    0
    """
    code = "s"
    assert walk(world, code) == "x"

    world = """
    1
    """
    code = "s"
    assert walk(world, code) == "x"

    world = """
    2
    """
    code = "s"
    assert walk(world, code) == "x"

    world = """
    3
    """
    code = "s"
    assert walk(world, code) == "x"


def test_simple():
    world = """
    ...
    .0.
    ...
    """
    code = "ss"
    assert walk_position(world, code) == ("sx", (0, 1))

    world = """
    ...
    .1.
    ...
    """
    code = "ss"
    assert walk_position(world, code) == ("sx", (1, 2))

    world = """
    ...
    .2.
    ...
    """
    code = "ss"
    assert walk_position(world, code) == ("sx", (2, 1))

    world = """
    ...
    .3.
    ...
    """
    code = "ss"
    assert walk_position(world, code) == ("sx", (1, 0))


def test_turns():
    world = """
    ...
    .0.
    ...
    """
    code = "rrrrllll"
    assert walk_position(world, code) == ("rrrrllll", (1, 1))

    world = """
    ...
    .0.
    ...
    """
    code = "srrrrllll"
    assert walk_position(world, code) == ("srrrrllll", (0, 1))

    world = """
    ...
    .0.
    ...
    """
    code = "ssrrrrllll"
    assert walk_position(world, code) == ("sxrrrrllll", (0, 1))


def test_stars():
    world = """
    .*.
    .0.
    ...
    """
    code = "s"
    assert walk_position_solved(world, code) == ("s", (0, 1), True)

    world = """
    .*.
    .1.
    ...
    """
    code = "s"
    assert walk_position_solved(world, code) == ("s", (1, 2), False)

    world = """
    .*.
    *0*
    .*.
    """
    code = """
    srsrssrssrss
    """
    assert walk_position_solved(world, code) == ("srsrssrssrss", (0, 0), True)