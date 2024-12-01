from collections import defaultdict

left, right = [], []
appearances = defaultdict(int)

with open('in/01.txt') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)
        appearances[b] += 1
    
left.sort()
right.sort()

# 1st star
print(sum([abs(a - b) for a, b in zip(left, right)]))

# 2nd star
print(sum([a * appearances[a] for a in left]))

