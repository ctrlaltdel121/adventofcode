import re

with open('3.input') as input:
    content = input.readlines()

# Capture groups for claim input format
claimRegex = re.compile(r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)')

# 1kx1k matrix
fabric = [[0 for x in range(1000)] for y in range(1000)] 


for claim in content:
    matches = claimRegex.match(claim)
    left =  int(matches.group(2))
    top = int( matches.group(3))
    wide =  int(matches.group(4))
    tall =  int(matches.group(5))

    # Fill in fabric matrix
    for x in range(left, left+wide):
        for y in range(top, top+tall):
            fabric[x][y] += 1

# Find number of matrix values incremented >1
countOverlap = 0
for x in fabric:
    for y in x:
        if y > 1:
            countOverlap+=1

print(countOverlap)


# Part 2 - just run a 2nd iteration and find the claim where all matrix values are currently 1
# this could be collapsed into the 1st iteration if we kept a claim set and removed each as we detected overlaps
def checkClaim(left, wide, top, tall, fabric):
    for x in range(left, left+wide):
        for y in range(top, top+tall):
            if fabric[x][y] != 1:
                return False
    return True


for claim in content:
    matches = claimRegex.match(claim)
    claimID = int(matches.group(1))
    left =  int(matches.group(2))
    top = int( matches.group(3))
    wide =  int(matches.group(4))
    tall =  int(matches.group(5))

    if checkClaim(left, wide, top, tall, fabric):
        print(claimID)
        break