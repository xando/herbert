from herbert import interpreter


def test_steps():
    assert interpreter.interpret("sss")['code'] == "sss"
    assert interpreter.interpret("rsss")['code'] == "rsss"
    assert interpreter.interpret("sssl")['code'] == "sssl"


def test_multiline_steps():
    ret = interpreter.interpret("""
    ss
    sss
    """)

    assert ret["code"] == "sssss"


def test_function_simple():
    ret = interpreter.interpret("""
    f:sss
    f
    """)

    assert ret["code"] == "sss"
    assert ret["length"] == 5

    ret = interpreter.interpret("""
    z:rrr
    f:sss
    fz
    """)

    assert ret["code"] == "sssrrr"
    assert ret["length"] == 10

    ret = interpreter.interpret("""
    z:rrr
    f:sz
    f
    """)

    assert ret["code"] == "srrr"
    assert ret["length"] == 8


def test_function_arguments():
    ret = interpreter.interpret("""
    f(A):A
    f(ss)
    """)

    assert ret["code"] == "ss"
    assert ret["length"] == 6

    ret = interpreter.interpret("""
    f(A,B):AB
    f(ss, rr)
    """)

    assert ret["code"] == "ssrr"
    assert ret["length"] == 10

    ret = interpreter.interpret("""
    f(A):llA
    ssf(rr)
    """)

    assert ret["code"] == "ssllrr"
    assert ret["length"] == 10

    ret = interpreter.interpret("""
    z(A):A
    f(A):lz(A)l
    ssf(rr)
    """)

    assert ret["code"] == "sslrrl"
    assert ret["length"] == 14


def test_function_depth():
    ret = interpreter.interpret("""
    f(A):sf(A-1)
    f(4)
    """)

    assert ret["code"] == "ssss"
    assert ret["length"] == 8

    ret = interpreter.interpret("""
    f(A, B):sf(A-1, B)B
    f(4, rr)
    """)

    assert ret["code"] == "ssssrrrrrrrr"
    assert ret["length"] == 13
