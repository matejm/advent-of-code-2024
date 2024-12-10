
from collections import defaultdict

with open('in/10.txt') as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

score = defaultdict(set)
score2 = defaultdict(int)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# first 9, then 8, then 7, etc
for height in range(9, 0, -1):
    # check all possible positions
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            # check if we have a number
            if grid[x][y] == height:
                # Update score of all neighbors (if they are height - 1)
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                        continue

                    if grid[nx][ny] == height - 1:
                        # add which 9s can we reach
                        if height == 9:
                            score[(nx, ny)].add((x, y))
                            score2[(nx, ny)] += 1
                        else:
                            score[(nx, ny)] |= score[(x, y)]
                            score2[(nx, ny)] += score2[(x, y)]


# total score of all zeros
total = 0
total2 = 0

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 0:
            total += len(score[(x, y)])
            total2 += score2[(x, y)]

# 1st star
print(total)

# 2nd star
print(total2)
