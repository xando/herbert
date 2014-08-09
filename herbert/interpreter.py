from . import parser
from . import ast


def walk_world(world, code):
    ret = []

    world = [[e for e in line] for line in world.split()]
    size = len(world)
    moves = (
        (-1, 0), (0, 1), (1, 0), (0, -1)
    )

    position = None
    direction = None

    for x in range(size):
        for y in range(size):
            if world[x][y] in ['0', '1', '2', '3']:
                position = (x, y)
                direction = int(world[x][y])

    for step in code:
        if step == 'r':
            direction = (direction + 1) % 4
            ret.append(str(direction))
            ret.append(step)

        elif step == 'l':
            ret.append(str(direction))
            direction = (direction - 1) % 4
            ret.append(step)

        elif step == 's':
            next_move = moves[direction]

            position = (
                position[0] + next_move[0],
                position[1] + next_move[1]
            )
            if position[0] >= 0 and position[0] < size and \
               position[1] >= 0 and position[1] < size and \
               world[position[0]][position[1]] in ['.', '*']:
                element = world[position[0]][position[1]]
                ret.append('s')
                if element == '*':
                    world[position[0]][position[1]] = '.'
            else:
                ret.append('x')
                position = (
                    position[0] - next_move[0],
                    position[1] - next_move[1]
                )

    success = True
    for line in world:
        if '*' in line:
            success = False

    return "".join(ret), position, success


def interpret(source, world=None):
    ret = {
        "code": "",
        "error": {}
    }
    try:
        ast_tree = parser.parse(source)
        ret['code'] = ast.eval(ast_tree, source)

    except ValueError as e:
        ret['error'] = e.message

    return ret
