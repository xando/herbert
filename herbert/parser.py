from rply import ParserGenerator
from rply.errors import LexingError

from . import ast
from . import lexer


pg = ParserGenerator(
    lexer.TOKENS,
    precedence=[
        ("nonassoc", ['NEWLINE', ')', 'COLON']),
        ("left", ['PLUS', 'MINUS'])
    ],
    cache_id="language"
)


@pg.production("main : line")
def _(p):
    return ast.Root([p[0]])


@pg.production("main : NEWLINE")
def _(p):
    return ast.Root([])


@pg.production("main : NEWLINE line")
def _(p):
    return ast.Root([p[1]])


@pg.production("main : main line")
def _(p):
    p[0].append(p[1])
    return p[0]


@pg.production("line : line-content NEWLINE ")
def _(p):
    return p[0]


@pg.production("line-content : moves-list ")
@pg.production("line-content : func-definition ")
def _(p):
    return p[0]


@pg.production("func-definition : FUNC COLON moves-list ")
def _(p):
    return ast.FuncDefinition(
        p[0].getstr(),
        p[2],
        None,
        p[0].getsourcepos()
    )


@pg.production("func-definition : FUNC ( def-args-list ) COLON moves-list ")
def _(p):
    return ast.FuncDefinition(
        p[0].getstr(),
        p[5],
        p[2].get_stmts(),
        p[0].getsourcepos()
    )


@pg.production("def-args-list : def-args-list , def-arg ")
def _(p):
    p[0].append(p[2])
    return p[0]


@pg.production("def-args-list : def-arg ")
def _(p):
    return ast.DefArgList([p[0]])


@pg.production("def-arg : NAME ")
def _(p):
    return ast.DefArg(p[0].getstr(), p[0].getsourcepos())


@pg.production("moves-list : moves-list move ")
def _(p):
    p[0].append(p[1])
    return p[0]


@pg.production("moves-list : move ")
def _(p):
    return ast.Line([p[0]])


@pg.production("move : variable ")
@pg.production("move : func-call ")
@pg.production("move : step ")
def _(p):
    return p[0]


@pg.production("variable : NAME ")
def _(p):
    return ast.Variable(p[0].getstr(), p[0].getsourcepos())


@pg.production("func-call : FUNC ")
def _(p):
    return ast.FuncCall(p[0].getstr(), None, p[0].getsourcepos())


@pg.production("func-call : FUNC ( args-list ) ")
def _(p):
    return ast.FuncCall(p[0].getstr(), p[2], p[0].getsourcepos())


@pg.production("args-list : args-list , arg ")
def _(p):
    p[0].append(p[2])
    return p[0]


@pg.production("args-list : arg ")
def _(p):
    return ast.CallArgList([p[0]])


@pg.production("arg : moves-list ")
def _(p):
    return p[0]


@pg.production("arg : expr ")
def _(p):
    return p[0]


@pg.production("expr : expr PLUS expr")
@pg.production("expr : expr MINUS expr")
def _(p):
    return ast.Expr(p[0], p[1].getstr(), p[2])


@pg.production("expr : NAME")
def _(p):
    return ast.Variable(p[0].getstr(), p[0].getsourcepos())


@pg.production("expr : NUMBER")
def _(p):
    return ast.Number(int(p[0].getstr()), p[0].getsourcepos())


@pg.production("step : STEP ")
@pg.production("step : TURN_LEFT ")
@pg.production("step : TURN_RIGHT ")
def _(p):
    return ast.Step(p[0].getstr(), p[0].getsourcepos())


@pg.error
def error_handler(token):
    line = token.source_pos.lineno
    column = token.source_pos.colno

    raise ValueError('(%s:%s) Ran into a "%s" where it wasn\'t expected.' % (
        line, column, token.gettokentype())
    )


parser = pg.build()

class color:
    RED = '\033[91m'
    END = '\033[0m'


def parse(source):
    source = "%s\n" % source

    try:
        token_stream = lexer.lexer.lex(source)
        return parser.parse(token_stream)
    except LexingError:
        colno = token_stream.idx -source.rfind("\n", 0, token_stream.idx)
        lineno = token_stream._lineno

        line = source.split("\n")[lineno - 1]
        code = []
        for i, c in enumerate(line):
            if i == colno - 1:
                code.append(color.RED + c + color.END)
            else:
                code.append(c)

        error = {
            "location": "Line:%s, Column:%s" % (lineno, colno),
            "message": "Lexer error",
            "help": "%s\n%s" % (
                "".join(code),
                color.RED + "-" * (colno - 1) + '^' + color.END
            )
        }

        raise ValueError(error)
