import os
import time

grid = []
moves = ''

robot = None

expanded_grid = []
expanded_robot = None

with open('in/15.txt') as f:
    grid_lines = True

    for index, line in enumerate(f.readlines()):
        if line.strip() == '':
            grid_lines = False
            continue

        if grid_lines:
            line = line.strip()
            expanded_line = line.replace('.', '..').replace(
                '#', '##').replace('O', '[]').replace('@', '@.')

            line = list(line)
            expanded_line = list(expanded_line)

            if '@' in line:
                robot = [index, line.index('@')]
                line[line.index('@')] = '.'

            if '@' in expanded_line:
                expanded_robot = [index, expanded_line.index('@')]
                expanded_line[expanded_line.index('@')] = '.'

            grid.append(line)
            expanded_grid.append(expanded_line)
        else:
            moves += line.strip()


def move_to_direction(move):
    if move == '^':
        return (-1, 0)
    elif move == '>':
        return (0, 1)
    elif move == 'v':
        return (1, 0)
    elif move == '<':
        return (0, -1)


def can_move(robot, direction):
    what = grid[robot[0] + direction[0]][robot[1] + direction[1]]
    if what == '.':
        return True
    elif what == '#':
        return False
    elif what == 'O':
        # We need to check if O can move
        if can_move((
            robot[0] + direction[0],
            robot[1] + direction[1]
        ), direction):
            # Then move it and tell that we can move robot
            grid[robot[0] + 2 * direction[0]][robot[1] + 2 * direction[1]] = 'O'
            grid[robot[0] + direction[0]][robot[1] + direction[1]] = '.'
            return True

        return False

    assert False


def can_move_expanded(robot, direction):
    what = expanded_grid[robot[0] + direction[0]][robot[1] + direction[1]]
    if what == '.':
        return True, lambda: None
    elif what == '#':
        return False, lambda: None
    elif what == '[' or what == ']':
        # If direction is left or right, this is still quite easy
        if direction[0] == 0:
            # We need to check if box [] can move (check two fields away, not only one as box is wide)
            can, execute = can_move_expanded((
                robot[0] + 2 * direction[0],
                robot[1] + 2 * direction[1]
            ), direction)

            if can:
                # Then move it and tell that we can move robot
                def execute_move():
                    execute()
                    expanded_grid[robot[0] + 2 * direction[0]][robot[1] + 2 *
                                                               direction[1]] = '[' if direction[1] > 0 else ']'
                    expanded_grid[robot[0] + 3 * direction[0]][robot[1] + 3 *
                                                               direction[1]] = ']' if direction[1] > 0 else '['
                    expanded_grid[robot[0] + direction[0]
                                  ][robot[1] + direction[1]] = '.'
                return True, execute_move

            return False, lambda: None
        else:
            # We need to check if box [] can move up or down (we need to check both fields)

            # represents position of [
            left_part = [robot[0] + direction[0], robot[1] + direction[1]]
            # represents position of ]
            right_part = [robot[0] + direction[0], robot[1] + direction[1]]
            if what == '[':
                right_part[1] += 1
            else:
                left_part[1] -= 1

            can1, execute1 = can_move_expanded(left_part, direction)
            can2, execute2 = can_move_expanded(right_part, direction)

            if can1 and can2:
                # Then move it and tell that we can move robot
                def execute_move():
                    execute1()
                    execute2()

                    expanded_grid[left_part[0] +
                                  direction[0]][left_part[1]] = '['
                    expanded_grid[right_part[0] +
                                  direction[0]][right_part[1]] = ']'
                    # Clean up
                    expanded_grid[left_part[0]][left_part[1]] = '.'
                    expanded_grid[right_part[0]][right_part[1]] = '.'
                return True, execute_move

            return False, lambda: None

    assert False


def move(robot, direction):
    if can_move(robot, direction):
        robot[0] += direction[0]
        robot[1] += direction[1]

    return robot


def move_expanded(robot, direction):
    can, execute = can_move_expanded(robot, direction)
    if can:
        execute()
        robot[0] += direction[0]
        robot[1] += direction[1]

    return robot


for m in moves:
    robot = move(robot, move_to_direction(m))

gps_score = 0

# Get total score
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'O':
            gps_score += 100 * y + x

# 1st star
print(gps_score)

for m in moves:
    expanded_robot = move_expanded(expanded_robot, move_to_direction(m))

    os.system('clear')
    for i, line in enumerate(expanded_grid):
        if i == expanded_robot[0]:
            line[expanded_robot[1]] = '@'
            print(''.join(line))
            line[expanded_robot[1]] = '.'
        else:
            print(''.join(line))
    time.sleep(0.05)


gps_score = 0

# Get total score
for y in range(len(expanded_grid)):
    for x in range(len(expanded_grid[0])):
        if expanded_grid[y][x] == '[':
            gps_score += 100 * y + x

# 2nd star
print(gps_score)
