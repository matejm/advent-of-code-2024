import sys
sys.setrecursionlimit(10000)

grid = []

start = None

visited = set()
visited_with_direction = set()


with open('in/06.txt') as f:
    for i, line in enumerate(f.readlines()):
        if not line.strip():
            continue

        line = line.strip()
        if '^' in line:
            start = i, line.find('^')
            line = line.replace('^', '.')

        grid.append(list(line))


def rotate(direction):
    return (direction[1], -direction[0])


def simulate(position, direction):
    visited.add(position)

    if (position, direction) in visited_with_direction:
        return 'cycle'

    visited_with_direction.add((position, direction))

    i, j = position
    di, dj = direction
    next_i, next_j = i + di, j + dj
    if next_i < 0 or next_i >= len(grid) or next_j < 0 or next_j >= len(grid[0]):
        # Out of bounds
        return 'out of bounds'
    if grid[next_i][next_j] == '#':
        return simulate(position, rotate(direction))
    else:
        return simulate((next_i, next_j), direction)


# i = row, j = col
direction_up = (-1, 0)
simulate(start, direction_up)

# 1st star
print(len(visited))


cycles = 0

# Slow and stupid, but it works
for i in range(len(grid)):
    for j in range(len(grid[0])):
        visited.clear()
        visited_with_direction.clear()

        if grid[i][j] == '.':
            grid[i][j] = '#'

            what = simulate(start, direction_up)

            if what == 'cycle':
                cycles += 1

            # revert
            grid[i][j] = '.'

# 2nd star
print(cycles)
