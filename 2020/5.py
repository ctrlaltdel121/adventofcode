import re

with open('5.input') as f:
    input = f.readlines()

seats = set()
for seat in input:
    low = 0
    high = 128
    left = 0
    right = 8
    row = 0
    col = 0
    for i, c in enumerate(seat):
        if c == "F":
            high = high - (high-low)/2
        if c == "B":
            low = low + (high-low)/2
        if c == "L":
            right = right - (right-left)/2
        if c == "R":
            left = left + (right-left)/2
        if i == 6 and c == "F":
            row = high - 1
        elif i == 6 and c == "B":
            row = low
        elif i == 9 and c == "L":
            col = left
        elif i == 9 and c == "R":
            col = right - 1
    seats.add(int(row*8+col))

print("Part 1: ", max(seats))

for i in range(max(seats)):
    if (i not in seats) and (i+1 in seats) and (i-1 in seats):
        print("Part 2: ", i)
