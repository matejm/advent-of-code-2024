from math import gcd


with open('in/13.txt') as f:
    lines = f.readlines()

machines = []

for i in range(0, len(lines), 4):
    ax, ay = map(int, lines[i].split('A:')[1].replace(
        'X+', '').replace('Y+', '').split(','))
    bx, by = map(int, lines[i + 1].split('B:')[1].replace(
        'X+', '').replace('Y+', '').split(','))
    px, py = map(int, lines[i + 2].split('Prize:')[1].replace(
        'X=', '').replace('Y=', '').split(','))

    machines.append(
        ((ax, ay), (bx, by), (px, py))
    )


def find_best_price(a, b, prize):
    options = []

    for a_count in range(0, max(prize[0] // a[0], prize[1] // a[1]) + 1):
        # check how many b's are needed
        remaining_x = prize[0] - a[0] * a_count
        remaining_y = prize[1] - a[1] * a_count

        # check if this is a valid solution
        if remaining_x % b[0] != 0 or remaining_y % b[1] != 0:
            continue

        # calculate the number of b's needed
        b_count_candidate = remaining_x // b[0]
        b_count_candidate2 = remaining_y // b[1]

        if b_count_candidate == b_count_candidate2:
            options.append((a_count, b_count_candidate))

    # return the best option
    if not options:
        return None

    best = 0
    for a_count, b_count in options:
        best = max(best, 3 * a_count + b_count)

    return best


def find_best_price_smart(a, b, prize):
    # linear diophantic equation
    has_solution_x = prize[0] % gcd(a[0], b[0]) == 0
    has_solution_y = prize[1] % gcd(a[1], b[1]) == 0

    if not has_solution_x or not has_solution_y:
        return None

    # egcd was not the solution, opened reddit and found this is a normal system of 2 equations
    # | a0 b0 | | A |  = | prize x |
    # | a1 b1 | | B |    | prize y |

    A = prize[0] * b[1] - b[0] * prize[1]
    B = - prize[0] * a[1] + a[0] * prize[1]

    # to complete inverse we need to divide
    denom = a[0] * b[1] - a[1] * b[0]

    if A % denom != 0:
        return None
    if B % denom != 0:
        return None

    A //= denom
    B //= denom

    return 3 * A + B


total = 0

for a, b, prize in machines:
    best = find_best_price(a, b, prize)
    if best is not None:
        total += best

# 1st star
print(total)

total = 0

# increase the prize
for a, b, prize in machines:
    best = find_best_price_smart(
        a, b, (prize[0] + 10000000000000, prize[1] + 10000000000000))
    if best is not None:
        total += best

# 2nd star
print(total)
