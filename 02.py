from collections import defaultdict

safe = []


def is_safe(l: list):
    increasing = True
    decreasing = True

    for i in range(len(l) - 1):
        diff = l[i + 1] - l[i]
        if not (0 < diff <= 3):
            increasing = False
        if not (-3 <= diff < 0):
            decreasing = False

    return increasing or decreasing


def is_partially_safe(l: list):
    # Far from efficient, but simple to code
    return any([
        is_safe(l[:i] + l[i + 1:]) for i in range(len(l))
    ])


total_safe = 0
total_partially_safe = 0

with open('in/02.txt') as f:
    for line in f.readlines():
        if not line:
            continue

        numbers = list(map(int, line.split()))
        total_safe += is_safe(numbers)
        total_partially_safe += is_partially_safe(numbers)


# 1st star
print(total_safe)

# 2nd star
print(total_partially_safe)
