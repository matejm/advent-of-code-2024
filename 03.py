import re

with open('in/03.txt') as f:
    line = ''.join(f.readlines())

res = re.findall(r'mul\([0-9]+,[0-9]+\)', line)


def evaluate(mul):
    m = re.match(r"mul\(([0-9]+),([0-9]+)\)", mul)
    a = m.group(1)
    b = m.group(2)
    return int(a) * int(b)


# 1st star
print(sum(map(evaluate, res)))

res2 = re.findall(r'(mul\([0-9]+,[0-9]+\))|(do\(\))|(don\'t\(\))', line)

s = 0
on = True
for e in res2:
    if e[1] == 'do()':
        on = True
    elif e[2] == 'don\'t()':
        on = False
    else:
        if on:
            s += evaluate(e[0])

# 2nd star
print(s)
