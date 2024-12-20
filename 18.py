with open('in/18.txt') as f:
    positions = list(
        map(lambda x: tuple(map(int, x.split(','))), f.readlines()))

size = 71
number_of_positions = 1024

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid = [['.' for _ in range(size)] for _ in range(size)]

for x, y in positions[:number_of_positions]:
    grid[y][x] = '#'


def bfs(grid, start, end):
    queue = [(0, start)]
    visited = set()
    visited.add(start)

    while queue:
        distance, pos = queue.pop(0)
        if pos == end:
            return distance

        for dx, dy in directions:
            x, y = pos
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue

            if grid[ny][nx] != '#' and (nx, ny) not in visited:
                queue.append((distance + 1, (nx, ny)))
                visited.add((nx, ny))

    return None


# 1st star
print(bfs(grid, (0, 0), (size - 1, size - 1)))

# add positions until we don't find a path
for pos in positions[number_of_positions:]:
    grid[pos[1]][pos[0]] = '#'
    # If this is slow, we can memoize the path and retry
    # the bfs only if we blocked the path
    distance = bfs(grid, (0, 0), (size - 1, size - 1))
    if distance is None:
        # 2nd star
        print(','.join(map(str, pos)))
        break
