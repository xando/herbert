import re

from . import parser
from . import ast

rx = re.compile("\(|\)|\s|\n|\:|\,|\-|\+")

def interpret(source, world=None):
    ret = {
        "code": "",
        "error": {}
    }
    try:
        ast_tree = parser.parse(source)
        ret['code'] = ast.eval(ast_tree, source)
        ret['length'] = len(rx.sub('', source))
    except ValueError as e:
        ret['error'] = e.message

    return ret
