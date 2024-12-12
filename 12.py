from collections import defaultdict, deque

with open('in/12.txt') as f:
    garden = [line.strip() for line in f.readlines() if line.strip()]

visited = set()

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_double_edge_count(x, y, direction, additional_check=True):
    # Strategy:
    # - assign 2 points to single border edge
    # - assign 1 point to corner of longer edge
    # - assign 0 points to middle of longer edge
    # Example
    # .......
    # ...A...  <- checking at position of A, direction is (-1, 0) looking up
    #             We check left and right neighbors and see this is a 1 length edge.
    # .......
    # ..AA...  <- this is a 2 length edge, we assign 1 point to each corner, again 2 total
    # .......
    #
    # ...A...
    # ..AA...  <- 2 points because this is a corner (looking at leftmost A)

    n1x, n1y = (direction[1], direction[0])
    n2x, n2y = (-direction[1], -direction[0])

    def check(original, d_neighbor, d_diagonal):
        a = garden[original[0]][original[1]]

        b = None
        if not (original[0] + d_neighbor[0] < 0 or original[1] + d_neighbor[1] < 0 or original[0] + d_neighbor[0] >= len(garden) or original[1] + d_neighbor[1] >= len(garden[0])):
            b = garden[original[0] + d_neighbor[0]
                       ][original[1] + d_neighbor[1]]

        c = None
        if not (original[0] + d_diagonal[0] < 0 or original[1] + d_diagonal[1] < 0 or original[0] + d_diagonal[0] >= len(garden) or original[1] + d_diagonal[1] >= len(garden[0])):
            c = garden[original[0] + d_diagonal[0]
                       ][original[1] + d_diagonal[1]]

        if a == b and a != c:
            return 0
        return 1

    return (check((x, y), (n1x, n1y), (n1x + direction[0], n1y + direction[1])) +
            check((x, y), (n2x, n2y), (n2x + direction[0], n2y + direction[1])))


def count_border(x, y):
    borders = 0
    double_edge_count = 0
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= len(garden) or ny >= len(garden[0]):
            borders += 1
            double_edge_count += get_double_edge_count(x, y, (dx, dy))
        elif garden[nx][ny] != garden[x][y]:
            borders += 1
            double_edge_count += get_double_edge_count(x, y, (dx, dy))
    return borders, double_edge_count


total = 0
total2 = 0

for start_x in range(len(garden)):
    for start_y in range(len(garden[0])):
        if (start_x, start_y) in visited:
            continue

        x, y = start_x, start_y

        # visit the region
        area = 1
        perimeter, double_edge_count = count_border(x, y)

        visited.add((x, y))

        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= len(garden) or ny >= len(garden[0]):
                    continue
                if garden[nx][ny] == garden[x][y] and (nx, ny) not in visited:
                    area += 1
                    border, de_count = count_border(nx, ny)
                    perimeter += border
                    double_edge_count += de_count

                    visited.add((nx, ny))
                    queue.append((nx, ny))

        total += area * perimeter
        total2 += area * double_edge_count


# 1st star
print(total)

# 2nd star
print(total2 // 2)
