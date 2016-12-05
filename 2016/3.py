#!/usr/bin/python
# To run, specify arg of 1 for part 1 or 2 for part 2.
import sys

INPUT_FILE = "3_1.input"


def check_side(a, b, c):
    return (int(a) + int(b)) > int(c)


def get_possible(lines):
    # lines is either three lines (vertical triangles) or one (horizontal)
    if len(lines) == 1:
        spl = lines[0].split()
        if len(spl) != 3:
            raise "Something went wrong"
        if check_side(spl[0], spl[1], spl[2]) and check_side(spl[1], spl[2], spl[0]) and check_side(spl[0], spl[2], spl[1]):
            return 1
        else:
            return 0
    elif len(lines) == 3:
        possible_count = 0
        spl0 = lines[0].split()
        spl1 = lines[1].split()
        spl2 = lines[2].split()
        if check_side(spl0[0], spl1[0], spl2[0]) and check_side(spl1[0], spl2[0], spl0[0]) and check_side(spl0[0], spl2[0], spl1[0]):
            possible_count += 1
        if check_side(spl0[1], spl1[1], spl2[1]) and check_side(spl1[1], spl2[1], spl0[1]) and check_side(spl0[1], spl2[1], spl1[1]):
            possible_count += 1
        if check_side(spl0[2], spl1[2], spl2[2]) and check_side(spl1[2], spl2[2], spl0[2]) and check_side(spl0[2], spl2[2], spl1[2]):
            possible_count += 1
        return possible_count
    else:
        raise "Wrong number of lines passed to get_possible"


def run(lnum):
    possible_count = 0
    with open(INPUT_FILE) as infile:
        lines = []
        for line in infile:
            lines.append(line)
            if len(lines) == lnum:
                possible_count += get_possible(lines)
                lines = []
        # if len(lines) > 0:
        #     possible_count += get_possible(lines)
    print "There are %d possible triangles in the input" % possible_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Please specify 1 or 2 for which part to run"
    if sys.argv[1] == "1":
        run(1)
    elif sys.argv[1] == "2":
        run(3)
    else:
        print "Invalid part"
