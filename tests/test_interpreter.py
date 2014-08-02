from language import interpreter



def test_steps():
    assert interpreter.interpret("sss")['code'] == "sss"
    assert interpreter.interpret("rsss")['code'] == "rsss"
    assert interpreter.interpret("sssl")['code'] == "sssl"


def test_funcion():
    ret = interpreter.interpret("""
    f:sss
    f
    """)

    assert ret["code"] == "sss"

    ret = interpreter.interpret("""
    z:rrr
    f:sss
    fz
    """)

    assert ret["code"] == "sssrrr"

    ret = interpreter.interpret("""
    z:rrr
    f:sz
    f
    """)

    assert ret["code"] == "srrr"


def test_function_variable():
    ret = interpreter.interpret("""
    f(A):A
    f(ss)
    """)

    assert ret["code"] == "ss"

    ret = interpreter.interpret("""
    f(A,B):AB
    f(ss, rr)
    """)

    assert ret["code"] == "ssrr"

    ret = interpreter.interpret("""
    f(A):llA
    ssf(rr)
    """)

    assert ret["code"] == "ssllrr"

    ret = interpreter.interpret("""
    z(A):A
    f(A):lz(A)l
    ssf(rr)
    """)

    assert ret["code"] == "sslrrl"


def test_recursion_error():
    ret = interpreter.interpret("""
    f:f
    f
    """)

    assert ret['error']['location'] == 'Line:2, Column:7'
    assert ret['error']['message'] == 'Stack limit reached.'


def test_error_funcion_undefined():
    ret = interpreter.interpret("z")

    assert ret['error']['location'] == 'Line:1, Column:1'
    assert ret['error']['message'] == 'Function "z" is undefined.'

    ret = interpreter.interpret("""
    ssszf
    """)

    assert ret['error']['location'] == 'Line:2, Column:8'
    assert ret['error']['message'] == 'Function "z" is undefined.'


def test_error_funcion_arguments():
    ret = interpreter.interpret("""
    f(A):sA
    f
    """)

    assert ret['error']['location'] == 'Line:3, Column:5'
    assert ret['error']['message'] == 'Function "f" takes 1 arguments, 0 given.'

    ret = interpreter.interpret("""
    f(A,B):sAB
    f(ss)
    """)

    assert ret['error']['location'] == 'Line:3, Column:5'
    assert ret['error']['message'] == 'Function "f" takes 2 arguments, 1 given.'


def test_error_variable():
    ret = interpreter.interpret("""
    B
    """)

    assert ret['error']['location'] == 'Line:2, Column:5'
    assert ret['error']['message'] == 'Variable "B" is undefined.'

    ret = interpreter.interpret("""
    f:B
    sssf
    """)

    assert ret['error']['location'] == 'Line:2, Column:7'
    assert ret['error']['message'] == 'Variable "B" is undefined.'
