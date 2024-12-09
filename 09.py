from copy import deepcopy


def checksum(chunks):
    c = 0
    index = 0
    for chunk in chunks:
        for i in chunk:
            if i is None:
                index += 1
                continue
            c += index * i
            index += 1
    return c


with open('in/09.txt') as f:
    line = f.read().strip()


# Create chunks (we can generate them, largest will be 9)
chunks = []

id = 0
empty = False

for c in line:
    count = int(c)
    if empty:
        chunks.append([None] * count)
        id += 1
        empty = False
    else:
        chunks.append([id for _ in range(count)])
        empty = True

chunks2 = deepcopy(chunks)

# 1st star

filling_chunk = 1  # first is filled anyway
filling_from = chunks.pop()

while filling_chunk < len(chunks):
    # Get next non-empty chunk
    while len(filling_from) == 0 or all([x is None for x in filling_from]):
        filling_from = chunks.pop()

    if filling_chunk >= len(chunks):
        # We removed chunks
        break

    # Check if current chunk is empty, and if it is, fill it
    if any([x is None for x in chunks[filling_chunk]]):
        # Fill it
        for j in range(len(chunks[filling_chunk])):
            # If empty, fill it
            if chunks[filling_chunk][j] is None:
                # can pop from back, all are the same
                chunks[filling_chunk][j] = filling_from.pop()
            if not filling_from:
                break

    # if we filled that chunk, we can go to next one
    if not any([x is None for x in chunks[filling_chunk]]):
        filling_chunk += 1


# at the end, put filling_from back in (might not be ok)
chunks.append(filling_from)

# 1st star
print(checksum(chunks))

# 2nd star
chunks = chunks2

filling_from = len(chunks) - 1

while filling_from > 0:
    # Find large enough empty chunk
    for i in range(1, filling_from, 2):
        if sum([x is None for x in chunks[i]]) < len(chunks[filling_from]):
            # not enough space
            continue

        # Fill it
        idx = 0
        for j in range(len(chunks[i])):
            # If empty, fill it
            if chunks[i][j] is None:
                # can pop from back, all are the same
                chunks[i][j] = chunks[filling_from][idx]
                chunks[filling_from][idx] = None
                idx += 1

            if idx >= len(chunks[filling_from]):
                break

    # can skip empty chunks
    filling_from -= 2


# 2nd star
print(checksum(chunks))
