with open('in/20.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]

# Find start and end
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == 'S':
            start = (x, y)
            grid[y][x] = '.'
        if cell == 'E':
            end = (x, y)
            grid[y][x] = '.'

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(grid, start, end):
    queue = [(0, start)]
    visited = set()
    visited.add(start)
    distances = {start: 0}

    while queue:
        distance, pos = queue.pop(0)
        distances[pos] = distance
        if pos == end:
            return distance, distances

        for dx, dy in directions:
            x, y = pos
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                continue

            if grid[ny][nx] != '#' and (nx, ny) not in visited:
                queue.append((distance + 1, (nx, ny)))
                visited.add((nx, ny))


expected_distance, distances = bfs(grid, start, end)

# Simplest idea - just remove every block - slow
# for y in range(1, len(grid) - 1):
#     print(y, len(grid[y]))
#     for x in range(1, len(grid[0]) - 1):
#         if grid[y][x] == '#':
#             grid[y][x] = '.'

#             distance, _ = bfs(grid, start, end)
#             if distance <= expected_distance - save_at_least:

#                 number_of_cheats += 1

#             # Cleanup
#             grid[y][x] = '#'


def count_skips(save_at_least, skip_duration):
    number_of_cheats = 0
    # Simply check for every block - what is the most distance we can jump
    for from_block, from_block_distance in distances.items():
        for to_block, to_block_distance in distances.items():
            distance = abs(from_block[0] - to_block[0]) + \
                abs(from_block[1] - to_block[1])
            if distance > skip_duration:
                continue

            if from_block_distance + distance + save_at_least <= to_block_distance:
                number_of_cheats += 1

    return number_of_cheats


# 1st star
print(count_skips(100, 2))

# 2nd star
print(count_skips(100, 20))
