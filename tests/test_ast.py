from language import parser
from language import ast


def parse(code):
    return parser.parse(code)


def test_step():
    _ast = parse("""
    s
    """)

    assert _ast.lines[0] == ast.Line([
        ast.Step('s')
    ])

    _ast = parse("""
    ss
    """)

    assert _ast.lines[0] == ast.Line([
        ast.Step('s'),
        ast.Step('s')
    ])


def test_lines_step():

    _ast = parse("""
    ss
    rl
    """)

    assert _ast.lines[0] == ast.Line([
        ast.Step('s'),
        ast.Step('s')
    ])
    assert _ast.lines[1] == ast.Line([
        ast.Step('r'),
        ast.Step('l')
    ])


def test_lines_variable():

    _ast = parse("""
    A
    """)

    assert _ast.lines[0] == ast.Line([
        ast.Variable('A'),
    ])

    _ast = parse("""
    sAs
    """)

    assert _ast.lines[0] == ast.Line([
        ast.Step('s'),
        ast.Variable('A'),
        ast.Step('s')
    ])


def test_func_call():

    _ast = parse("""
    f
    """)

    assert _ast.lines[0] == ast.Line([ast.FuncCall('f')])

    _ast = parse("""
    sfs
    """)

    assert _ast.lines[0] == ast.Line([
        ast.Step('s'),
        ast.FuncCall('f'),
        ast.Step('s')
    ])


def test_func_call_args_moves():

    _ast = parse("""
    f(s)
    """)

    assert _ast.lines[0] == ast.Line([
        ast.FuncCall(
            'f',
            ast.CallArgList([
                ast.Line([ast.Step('s')])
            ])
        )
    ])


    _ast = parse("""
    f(sSs)
    """)

    assert _ast.lines[0] == ast.Line([
        ast.FuncCall(
            'f',
            ast.CallArgList([
                ast.Line([ast.Step('s'), ast.Variable('S'), ast.Step('s')])
            ])
        )
    ])


    _ast = parse("""
    f(s,F,sF)
    """)


    assert _ast.lines[0] == ast.Line([
        ast.FuncCall(
            'f',
            ast.CallArgList([
                ast.Line([ast.Step('s')]),
                ast.Line([ast.Variable('F')]),
                ast.Line([ast.Step('s'), ast.Variable('F')]),
            ])
        )
    ])


def test_func_def():

    _ast = parse("""
    f:ss
    """)

    assert _ast.lines[0] == ast.Line([
        ast.FuncDefinition('f', ast.Line([ast.Step('s'), ast.Step('s')]), None)
    ])

