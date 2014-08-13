

def walk(level, code, score):
    world = level['content']
    ret = []

    world = [[e for e in line] for line in world]
    size = len(world)
    moves = (
        (-1, 0), (0, 1), (1, 0), (0, -1)
    )

    position = None
    direction = None

    for x in range(size):
        for y in range(size):
            if world[x][y] in ['0', '1', '2', '3']:
                direction = int(world[x][y])
                position = (x, y)
                world[x][y] = "."

    for step in code:
        if step == 'r':
            direction = (direction + 1) % 4
            ret.append(step)
            ret.append(str(direction))

        elif step == 'l':
            direction = (direction - 1) % 4
            ret.append(step)
            ret.append(str(direction))

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

    rating = 0
    if success:
        limits = level.get('limits', [])
        limits.sort(reverse=True)

        for rate, limit in enumerate(level.get('limits', []), 1):
            if score <= limit:
                rating = rate

    return "".join(ret), position, rating
