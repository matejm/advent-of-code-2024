from functools import lru_cache

with open('in/19.txt') as f:
    lines = f.readlines()

    towels = list(lines[0].strip().split(', '))

    targets = [line.strip() for line in lines[1:] if line.strip()]


@lru_cache(maxsize=None)
def is_possible(target):
    if not target:
        return True

    # Try all possible combinations
    for towel in towels:
        if target[:len(towel)] == towel:
            # prefix matches, check suffix
            if is_possible(target[len(towel):]):
                return True

    return False


@lru_cache(maxsize=None)
def total_options(target):
    if not target:
        return 1

    total = 0
    for towel in towels:
        if target[:len(towel)] == towel:
            # prefix matches, check suffix
            total += total_options(target[len(towel):])

    return total


possible = 0

for target in targets:
    if is_possible(target):
        possible += 1

# 1st star
print(possible)


# 2nd star
total = 0

for target in targets:
    total += total_options(target)

print(total)
