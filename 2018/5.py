from collections import deque

with open('5.input') as f:
    input = f.read()

def process(line):
    queue = deque(line)
    finished = deque()

    while len(queue) > 1:
        if len(finished) > 0:
            x = finished.pop()
        else:
            x = queue.popleft() # startup case
        y = queue.popleft()
        if abs(ord(x)-ord(y)) == 32:
            if len(finished) > 0:
                queue.appendleft(finished.pop())
            continue
        else:
            finished.append(x)
            finished.append(y)

    return len(finished) + len(queue)

part1 = process(input)
print("Part 1:", part1)


# part 2
letters = 'abcdefghijklmnopqrstuvwxyz'
bestVal = 100000
for x in letters:
    myLine = input.replace(x, '').replace(x.upper(), '') # remove upper/lower case of each letter
    val = process(myLine)
    if val < bestVal:
        bestVal = val

print("Part 2:", bestVal)