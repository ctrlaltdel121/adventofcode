import re


with open('2.input') as f:
    input = f.readlines()

# part 1
dbRegex = re.compile(r'(\d*)-(\d*) (.): (.*)')
count = 0
for line in input:
    matches = dbRegex.match(line)
    minLetter = int(matches.group(1))
    maxLetter = int(matches.group(2))
    letter = matches.group(3)
    password = matches.group(4)
    if password.count(letter) >= minLetter and password.count(letter) <= maxLetter:
        count += 1


print("Part 1:", count)


count = 0
for line in input:
    matches = dbRegex.match(line)
    minLetter = int(matches.group(1))
    maxLetter = int(matches.group(2))
    letter = matches.group(3)
    password = matches.group(4)
    # 1-indexing
    minLetter = minLetter-1
    maxLetter = maxLetter-1
    if maxLetter >= len(password) or password[maxLetter] != letter:
        if password[minLetter] == letter:
            count += 1  # just minletter
        continue  # neither
    else:
        if password[minLetter] != letter:
            count += 1  # just maxLetter
        continue  # both


print("Part 2:", count)
