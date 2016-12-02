#!/usr/bin/python

INSTRUCTIONS = "L5, R1, L5, L1, R5, R1, R1, L4, L1, L3, R2, R4, L4, L1, L1, R2, R4, R3, L1, R4, L4, L5, L4, R4, L5, R1, R5, L2, R1, R3, L2, L4, L4, R1, L192, R5, R1, R4, L5, L4, R5, L1, L1, R48, R5, R5, L2, R4, R4, R1, R3, L1, L4, L5, R1, L4, L2, L5, R5, L2, R74, R4, L1, R188, R5, L4, L2, R5, R2, L4, R4, R3, R3, R2, R1, L3, L2, L5, L5, L2, L1, R1, R5, R4, L3, R5, L1, L3, R4, L1, L3, L2, R1, R3, R2, R5, L3, L1, L1, R5, L4, L5, R5, R2, L5, R2, L1, L5, L3, L5, L5, L1, R1, L4, L3, L1, R2, R5, L1, L3, R4, R5, L4, L1, R5, L1, R5, R5, R5, R2, R1, R2, L5, L5, L5, R4, L5, L4, L4, R5, L2, R1, R5, L1, L5, R4, L3, R4, L2, R3, R3, R3, L2, L2, L2, L1, L4, R3, L4, L2, R2, R5, L1, R2"

instruction_list = INSTRUCTIONS.split(", ")

x = 0
y = 0

visited = {}
foundVisitedTwice= (0,0)
 # N=0 E=1 S=2 W=3
direction = 0
for i in instruction_list:
	# Turn
	if i[0] == "L":
		direction = (direction - 1) % 4
	if i[0] == "R":
		direction = (direction + 1 ) % 4
	
	# move and record position
	size = int(i[1:])
	if direction == 0:
		for i in range(0,size):
			if foundVisitedTwice == (0,0):
				if (x, y) in visited:
					foundVisitedTwice = (x,y)
				else:
					visited[(x,y)] = True
			y+=1
		
	if direction == 1:
		for i in range(0,size):
			if foundVisitedTwice == (0,0):
				if (x, y) in visited:
					foundVisitedTwice = (x,y)
				else:
					visited[(x,y)] = True
			x+=1
	if direction == 2:
		for i in range(0,size):
			if foundVisitedTwice == (0,0):
				if (x, y) in visited:
					foundVisitedTwice = (x,y)
				else:
					visited[(x,y)] = True
			y-=1
	if direction == 3:
		for i in range(0,size):
			if foundVisitedTwice == (0,0):
				if (x, y) in visited:
					foundVisitedTwice = (x,y)
				else:
					visited[(x,y)] = True
			x-=1

print "The directions end at point (%d,%d) which is %d away from the start." %(x, y, abs(x) + abs(y))
print "The first place you visit twice is point (%d,%d) which is %d away from the start." %(foundVisitedTwice[0], foundVisitedTwice[1], abs(foundVisitedTwice[0]) + abs(foundVisitedTwice[1]))

