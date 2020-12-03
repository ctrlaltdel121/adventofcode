

with open('3.input') as f:
    input = f.readlines()

paths = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
total = 1
for (down, right) in paths:
    i = 0
    j = 0
    count = 0
    while i < len(input):
        line = input[i].strip()
        if line[j % len(line)] == "#":
            count += 1
        i += down
        j += right
    total = total * count
    if down == 1 and right == 3:
        print("Part 1:", count)

print("Part 2:", total)
