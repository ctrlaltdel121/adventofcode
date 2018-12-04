with open('2.input') as f:
    input = f.readlines()

# part 1
twos = 0
threes = 0
letters = 'abcdefghijklmnopqrstuvwxyz'
for line in input:
    hasTwo = False
    hasThree = False
    for l in letters:
        x = line.count(l)
        if x == 2: hasTwo = True
        if x == 3: hasThree = True
    if hasTwo: twos+=1
    if hasThree: threes+=1

print("Part 1:", twos*threes)


# Part 2
for x in input:
    for line in input:
        currentCountDiff = 0
        diffChar = ''
        for i, char in enumerate(line):
            if char != x[i]:
                currentCountDiff+=1
                diffChar = x[i]
        if currentCountDiff == 1:
            print("Part 2:", x.replace(char, ''))
            exit()