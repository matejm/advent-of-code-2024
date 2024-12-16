import heapq

start = None
end = None

with open('in/16.txt') as f:
    lines = f.readlines()

    maze = []
    for i, line in enumerate(lines):
        line = line.strip()
        if 'S' in line:
            start = i, line.index('S')
            line = line.replace('S', '.')
        if 'E' in line:
            end = i, line.index('E')
            line = line.replace('E', '.')

        maze.append(list(line))


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def rotate(direction, clockwise):
    if clockwise:
        return directions[(directions.index(direction) + 1) % 4]
    else:
        return directions[(directions.index(direction) - 1) % 4]


queue = []
visited = set()
heapq.heappush(queue, (0, start, (0, 1), [(start, (0, 1))]))
visited.add((start, (0, 1)))

best_path = []
best_paths_to = {}


def update_best_paths_to(position, direction, total, path):
    if (position, direction) not in best_paths_to:
        best_paths_to[(position, direction)] = (total, [path])
    else:
        if total < best_paths_to[(position, direction)][0]:
            # should not be possible
            best_paths_to[(position, direction)] = (total, [path])
        elif total == best_paths_to[(position, direction)][0]:
            best_paths_to[(position, direction)][1].append(path)


while len(queue) > 0:
    total, position, direction, path = heapq.heappop(queue)
    update_best_paths_to(position, direction, total, path)

    if position == end:
        best_path = path
        break

    # forward
    forward_position = (position[0] + direction[0],
                        position[1] + direction[1])
    if maze[forward_position[0]][forward_position[1]] != '#':
        update_best_paths_to(forward_position, direction,
                             total + 1, path + [(forward_position, direction)])
        if (forward_position, direction) not in visited:
            heapq.heappush(queue, (
                total + 1,
                forward_position,
                direction,
                path + [(forward_position, direction)]
            ))
            visited.add((forward_position, direction))

    # left
    direction_left = rotate(direction, clockwise=False)
    left_position = (position[0] + direction_left[0],
                     position[1] + direction_left[1])
    if maze[left_position[0]][left_position[1]] != '#':
        update_best_paths_to(left_position, direction_left,
                             total + 1001, path + [(left_position, direction_left)])
        if (left_position, direction_left) not in visited:
            heapq.heappush(queue, (
                total + 1001,
                left_position,
                direction_left,
                path + [(left_position, direction_left)]
            ))
            visited.add((left_position, direction_left))

    # right
    direction_right = rotate(direction, clockwise=True)
    right_position = (position[0] + direction_right[0],
                      position[1] + direction_right[1])
    if maze[right_position[0]][right_position[1]] != '#':
        update_best_paths_to(right_position, direction_right,
                             total + 1001, path + [(right_position, direction_right)])
        if (right_position, direction_right) not in visited:
            heapq.heappush(queue, (
                total + 1001,
                right_position,
                direction_right,
                path + [(right_position, direction_right)]
            ))
            visited.add((right_position, direction_right))


# 1st star
print(total)

all_tiles = set()
visited = set()

# Recursively put together all paths


def add_best_path(position, direction):
    visited.add((position, direction))
    # Add best path to this tile
    for path in best_paths_to[(position, direction)][1]:
        for p, d in path:
            all_tiles.add(p)
            if (p, d) in visited:
                continue
            visited.add((p, d))
            add_best_path(p, d)


for position, direction in best_path:
    all_tiles.add(position)
    add_best_path(position, direction)


# Mark all tiles
for tile in all_tiles:
    maze[tile[0]][tile[1]] = 'O'

# for line in maze:
#     print(''.join(line))

# 2nd star
print(len(all_tiles))
