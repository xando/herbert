from herbert import solve


def walk(level, code):
    code, _, _ = solve.walk(level, code, 0)
    return code


def walk_position(level, code):
    code, poistion, _ = solve.walk(level, code, 0)
    return code, poistion


def walk_position_solved(level, code, score):
    return solve.walk(level, code, score)


def test_starting_point():
    code = "s"

    level = {
        "content": ["0"]
    }
    assert walk(level, code) == "x"

    level = {
        "content": ["0"]
    }
    assert walk(level, code) == "x"

    level = {
        "content": ["2"]
    }
    assert walk(level, code) == "x"

    level = {
        "content": ["3"]
    }
    assert walk(level, code) == "x"


def test_simple_move():
    code = "ss"

    level = {
        "content": [
            "...",
            ".0.",
            "..."
        ]
    }
    assert walk_position(level, code) == ("sx", (0, 1))

    level = {
        "content": [
            "...",
            ".1.",
            "..."
        ]
    }
    assert walk_position(level, code) == ("sx", (1, 2))

    level = {
        "content": [
            "...",
            ".2.",
            "..."
        ]
    }
    assert walk_position(level, code) == ("sx", (2, 1))

    level = {
        "content": [
            "...",
            ".3.",
            "..."
        ]
    }
    assert walk_position(level, code) == ("sx", (1, 0))


def test_turns():
    level = {
        "content": [
            "...",
            ".0.",
            "..."
        ]
    }

    code = "rrrrllll"
    assert walk_position(level, code) == ("r1r2r3r0l3l2l1l0", (1, 1))

    code = "srrrrllll"
    assert walk_position(level, code) == ("sr1r2r3r0l3l2l1l0", (0, 1))

    code = "ssrrrrllll"
    assert walk_position(level, code) == ("sxr1r2r3r0l3l2l1l0", (0, 1))


def test_stars():
    level = {
        "content": [
            ".*.",
            ".0.",
            "..."
        ],
        "limits": [3, 2, 1]
    }
    code = "s"
    assert walk_position_solved(level, code, 0) == ("s", (0, 1), 3)


    level = {
        "content": [
            ".*.",
            ".1.",
            "..."
        ],
        "limits": [3, 2, 1]
    }
    code = "s"
    assert walk_position_solved(level, code, 0) == ("s", (1, 2), 0)

    level = {
        "content": [
            ".*.",
            "*0*",
            ".*."
        ],
        "limits": [3, 2, 1]
    }
    code = """
    srsrssrssrss
    """
    assert walk_position_solved(level, code, 3) == ("sr1sr2ssr3ssr0ss", (0, 0), 1)


def test_wall():
    level = {
        "content": [
            ".#.",
            "#0#",
            ".#."
        ],
    }
    code = "s"
    assert walk_position_solved(level, code, 1) == ("x", (1, 1), 0)
