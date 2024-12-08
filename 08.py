from collections import defaultdict

grid = []
frequencies = defaultdict(list)

with open('in/08.txt') as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()

        if not line:
            continue

        grid.append(line)

        for j, char in enumerate(line):
            if char != '.':
                frequencies[char].append((i, j))

antinodes = set()
antinodes2 = set()
h = len(grid)
w = len(grid[0])

# check all frequencies
for char, positions in frequencies.items():
    # all pairs of positions
    for i, j in positions:
        for i2, j2 in positions:
            di = i2 - i
            dj = j2 - j

            if di == 0 and dj == 0:
                continue

            # add antinodes, if in grid
            if i - di >= 0 and i - di < h and j - dj >= 0 and j - dj < w:
                antinodes.add((i - di, j - dj))
            if i2 + di >= 0 and i2 + di < h and j2 + dj >= 0 and j2 + dj < w:
                antinodes.add((i2 + di, j2 + dj))

            # for 2nd star
            antinodes2.add((i, j))
            antinodes2.add((i2, j2))

            k = 1
            while i - k * di >= 0 and i - k * di < h and j - k * dj >= 0 and j - k * dj < w:
                antinodes2.add((i - k * di, j - k * dj))
                k += 1

            k = 1
            while i2 + k * di >= 0 and i2 + k * di < h and j2 + k * dj >= 0 and j2 + k * dj < w:
                antinodes2.add((i2 + k * di, j2 + k * dj))
                k += 1

# 1st star
print(len(antinodes))

# 2nd star
print(len(antinodes2))
