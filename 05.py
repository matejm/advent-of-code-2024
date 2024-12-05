from collections import defaultdict
from copy import deepcopy

before = defaultdict(set)
after = defaultdict(set)

orders = []


def validate_order(order, before, after):
    edition = set(order)

    for node in order:
        if before[node].intersection(edition):
            return None

        for next in after[node]:
            before[next].remove(node)
        after[node] = set()

    # return middle node
    return order[len(order) // 2]


def fix_order(order, before, after):
    new_order = []

    candidates = set(order)

    # keep adding the ones we can

    while candidates:
        added = set()
        for c in candidates:
            if not before[c].intersection(candidates):
                # can add
                new_order.append(c)
                added.add(c)

                for next in after[c]:
                    before[next].remove(c)
                after[c] = set()

        candidates -= added

    return new_order[len(new_order) // 2]


with open('in/05.txt') as f:
    graph = True

    for line in f.readlines():
        if not line.strip():
            graph = False
            continue

        if graph:
            a, b = map(int, line.split("|"))
            after[a].add(b)
            before[b].add(a)
        else:
            orders.append(list(map(int, line.split(","))))


s = 0
s2 = 0

for order in orders:
    res = validate_order(order, deepcopy(before), deepcopy(after))
    if res is not None:
        s += res
    else:
        fixed = fix_order(order, deepcopy(before), deepcopy(after))
        s2 += fixed

# 1st star
print(s)

# 2nd star
print(s2)
