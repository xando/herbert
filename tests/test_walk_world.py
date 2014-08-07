from herbert import interpreter


def walk(world, code):
    return interpreter.walk_world(world, code)


def test_starting_point():
    world = """
    0
    """
    code = "s"
    assert walk(world, code) == ("x", (0,0))

    world = """
    1
    """
    code = "s"
    assert walk(world, code) == ("x", (0,0))

    world = """
    2
    """
    code = "s"
    assert walk(world, code) == ("x", (0,0))

    world = """
    3
    """
    code = "s"
    assert walk(world, code) == ("x", (0,0))


def test_simple():
    world = """
    ...
    .0.
    ...
    """
    code = "ss"
    assert walk(world, code) == ("sx", (0, 1))

    world = """
    ...
    .1.
    ...
    """
    code = "ss"
    assert walk(world, code) == ("sx", (1, 2))

    world = """
    ...
    .2.
    ...
    """
    code = "ss"
    assert walk(world, code) == ("sx", (2, 1))

    world = """
    ...
    .3.
    ...
    """
    code = "ss"
    assert walk(world, code) == ("sx", (1, 0))
