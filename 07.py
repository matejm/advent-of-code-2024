results = []
options = []


def evaluate(current, options, target, allow_concatenation=False):
    if len(options) == 0:
        if current == target:
            return True
        return False

    next_option = options[0]
    remaining_options = options[1:]

    if current + next_option <= target and evaluate(current + next_option, remaining_options,
                                                    target, allow_concatenation=allow_concatenation):
        return True
    if current * next_option <= target and evaluate(current * next_option, remaining_options,
                                                    target, allow_concatenation=allow_concatenation):
        return True
    if allow_concatenation and int(f'{current}{next_option}') <= target and evaluate(
            int(f'{current}{next_option}'), remaining_options, target, allow_concatenation=allow_concatenation):
        return True

    return False


with open('in/07.txt') as f:
    for line in f.readlines():
        if not line.strip():
            continue

        line = line.strip().split(": ")
        results.append(int(line[0]))
        options.append(list(map(int, line[1].split())))

total = 0
total_concat = 0

for i in range(len(results)):
    possible = evaluate(options[i][0], options[i][1:], results[i])
    if possible:
        total += results[i]
    else:
        possible2 = evaluate(
            options[i][0], options[i][1:], results[i], allow_concatenation=True)
        if possible2:
            total_concat += results[i]

# 1st star
print(total)

# 2nd star
print(total + total_concat)
