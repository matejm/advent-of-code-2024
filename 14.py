import os
import time

with open('in/14.txt') as f:
    lines = f.readlines()

initial_positions = []
velocities = []

for line in lines:
    p, v = line.split()
    p = tuple(map(int, p.replace('p=', '').split(',')))
    v = tuple(map(int, v.replace('v=', '').split(',')))

    initial_positions.append(p)
    velocities.append(v)

positions = initial_positions[:]

w = 101
h = 103

for i in range(100):
    # move all robots
    for robot in range(len(positions)):
        positions[robot] = (
            (positions[robot][0] + velocities[robot][0]) % w,
            (positions[robot][1] + velocities[robot][1]) % h,
        )

grid = [[0 for _ in range(h)] for _ in range(w)]

for i in range(len(positions)):
    grid[positions[i][0]][positions[i][1]] += 1

# Count in quadrants
q = [0, 0, 0, 0]

for i in range(w):
    for j in range(h):
        if w // 2 == i or h // 2 == j:
            # center
            continue
        elif i < w // 2 and j < h // 2:
            # top left
            q[0] += grid[i][j]
        elif i < w // 2 and j > h // 2:
            # top right
            q[1] += grid[i][j]
        elif i > w // 2 and j < h // 2:
            # bottom left
            q[2] += grid[i][j]
        elif i > w // 2 and j > h // 2:
            # bottom right
            q[3] += grid[i][j]


print(q[0] * q[1] * q[2] * q[3])

positions = initial_positions[:]

# Repeat and visualize
for i in range(10000):
    # move all robots
    for robot in range(len(positions)):
        positions[robot] = (
            (positions[robot][0] + velocities[robot][0]) % w,
            (positions[robot][1] + velocities[robot][1]) % h,
        )

    grid = [[0 for _ in range(w)] for _ in range(h)]

    for j in range(len(positions)):
        grid[positions[j][1]][positions[j][0]] += 1

    # Display, but only we think they have a chance
    # 326
    # 427
    # 528
    if (i - 123) % 101 == 0 and i >= 7000:
        os.system('clear')
        print('Iteration', i + 1)

        for j in range(h):
            print(
                ''.join(map(str, map(lambda x: x if x > 0 else ' ', grid[j]))))

        input()
