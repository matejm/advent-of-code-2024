with open('in/17.txt') as f:
    lines = f.readlines()

A = int(lines[0].split(':')[1])
B = int(lines[1].split(':')[1])
C = int(lines[2].split(':')[1])

program = list(map(int, lines[4].split(':')[1].split(',')))


def combo(x, A, B, C):
    if x <= 3:
        return x
    if x == 4:
        return A
    if x == 5:
        return B
    if x == 6:
        return C

    assert False


def evaluate(program, A, B, C, expected=None):
    i = 0
    out = []

    while i < len(program):
        if program[i] == 0:
            # adv
            A = A // 2 ** combo(program[i + 1], A, B, C)
        elif program[i] == 1:
            # bxl
            B ^= program[i + 1]
        elif program[i] == 2:
            # bst
            B = combo(program[i + 1], A, B, C) % 8
        elif program[i] == 3:
            # jnz
            if A != 0:
                i = program[i + 1]
                continue
        elif program[i] == 4:
            # bxc
            B ^= C
        elif program[i] == 5:
            # out
            res = combo(program[i + 1], A, B, C) % 8

            if expected is not None and res != expected[len(out)]:
                return out

            out.append(res)
        elif program[i] == 6:
            # bdv
            B = A // (2 ** combo(program[i + 1], A, B, C))
        elif program[i] == 7:
            # cdv
            C = A // (2 ** combo(program[i + 1], A, B, C))
        else:
            assert False

        i += 2

    return out


# 1st star
out = evaluate(program, A, B, C)
print(','.join(map(str, out)))


# 2nd star
best = 0

# Check until 100000000: best 7
# Check until 1000000000: best 8 - 137505178

# At least 7:
# [1001531802,
# 1001630106,
# 1005726106,
# 1005824410,
# 1009920410,
# 1010018714,
# 1014114714,
# 1014213018,
# 1018276250,
# 1018309018,
# 1018407322,
# 1022503322,
# 1022601626,
# 1023502746,
# 1025599898,
# 1026632090,
# 1026648474,
# 1026697626,
# 1026795930,
# 1030891930,
# 1030990234,]

# At least 10
# 47113709978,
# 47113808282,
# 49009535386,
# 49009633690,
# 51140241818,
# 51140340122,
# 51157019034,
# 51157117338,
# 51408677274,
# 51408775578,
# 53304502682,
# 53304600986,
# 55435209114,
# 55435307418,
# 55451986330,
# 55452084634,
# 55703644570,
# 55703742874,
# 57599469978,
# 57599568282,
# 59730176410,

# A = 1001531802
A = 46845274522
step_index = 0

steps = [98304, 16678912, 98304, 251559936,
         98304, 1895727104, 98304, 2130608128]

while True:
    if A % 100000000 == 0:
        print('Progress:', A)

    out = evaluate(program, A, B, C, expected=program)
    if len(out) == len(program):
        if out == program:
            print('Result:', A)
            break
    else:
        match = len(out)
        if match > best:
            best = match
            print('Better match:', A, '(len:', match, ' out of ', len(program), ')')
        # elif match >= 10:
        #     print('At least 10:', A)

    A += steps[step_index]
    step_index = (step_index + 1) % len(steps)
