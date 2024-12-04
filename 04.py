from collections import defaultdict

grid = []

directions = [(-1, 0), (0, -1), (1, 0), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

target = list('XMAS')

x_mas_targets = [
    # M . S
    # . A .
    # M . S
    [
        ('M', (0, 0)),
        ('S', (0, 2)),
        ('A', (1, 1)),
        ('M', (2, 0)),
        ('S', (2, 2)),
    ],
    # M . M
    # . A .
    # S . S
    [
        ('M', (0, 0)),
        ('M', (0, 2)),
        ('A', (1, 1)),
        ('S', (2, 0)),
        ('S', (2, 2)),
    ],
    # S . M
    # . A .
    # S . M
    [
        ('S', (0, 0)),
        ('M', (0, 2)),
        ('A', (1, 1)),
        ('S', (2, 0)),
        ('M', (2, 2)),
    ],
    # S . S
    # . A .
    # M . M
    [
        ('S', (0, 0)),
        ('S', (0, 2)),
        ('A', (1, 1)),
        ('M', (2, 0)),
        ('M', (2, 2)),
    ],
]


def search(i, j, target, direction):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return False
    if grid[i][j] != target[0]:
        return False

    if len(target) == 1:
        return True

    return search(i + direction[0], j + direction[1], target[1:], direction)


def search2(i, j, target):
    for char, (di, dj) in target:
        if i + di < 0 or i + di >= len(grid) or j + dj < 0 or j + dj >= len(grid[0]):
            return False
        if grid[i + di][j + dj] != char:
            return False
    return True


with open('in/04.txt') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        grid.append(list(line.strip()))


total = 0
total2 = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        for direction in directions:
            total += search(i, j, target, direction)
        for x_mas_target in x_mas_targets:
            total2 += search2(i, j, x_mas_target)


# 1st star
print(total)

# 2nd star
print(total2)
