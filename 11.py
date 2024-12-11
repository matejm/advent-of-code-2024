from functools import lru_cache

with open('in/11.txt') as f:
    line = f.readline().strip()

initial_stones = list(map(int, line.split()))
stones = initial_stones[:]


def next_round(stones):
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            new_stones.append(int(s[: len(s) // 2]))
            new_stones.append(int(s[len(s) // 2:]))
        else:
            new_stones.append(stone * 2024)

    return new_stones


for i in range(25):
    stones = next_round(stones)


# 1st star
print(len(stones))

# we need a faster way to do this


@lru_cache(maxsize=None)
def expand_stone(stone: int, iterations: int) -> int:
    if iterations == 0:
        return 1

    new_stones = next_round([stone])
    return sum([
        expand_stone(stone, iterations - 1)
        for stone in new_stones
    ])


# 2nd star
print(sum([
    expand_stone(stone, 75)
    for stone in initial_stones
]))
