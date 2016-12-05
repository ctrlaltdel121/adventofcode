from collections import defaultdict
import re

INPUT_FILE = "4.input"
REGEX = re.compile('(.+)-(.*)\[(.*)\]')
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def is_real(name, checksum):
    counts = defaultdict(int)
    n = name.replace("-", "")
    for c in n:
        counts[c] += 1
    # this sort sorts by negative count (to reverse it)
    # and then forward by letter
    sorted_list = sorted(counts.items(), key=lambda tup: (-1 * tup[1], tup[0]))
    for i in range(0, 5):
        if sorted_list[i][0] != checksum[i]:
            return False
    return True


def decrypt(cipher, num):
    result = []
    for i in cipher:
        if i == "-":
            result.append(" ")
        else:
            result.append(ALPHABET[(ALPHABET.index(i) + num) % 26])
    return "".join(result)


def main():
    sector_sum = 0
    with open(INPUT_FILE) as inputfile:
        for line in inputfile:
            m = REGEX.match(line)
            if is_real(m.group(1), m.group(3)):
                sector_sum += int(m.group(2))
                d = decrypt(m.group(1), int(m.group(2)))
                if "northpole" in d:
                    print "North pole storage ID: %s" % m.group(2)

    print "Total sum of valid sector IDs: %d" % sector_sum

if __name__ == "__main__":
    main()
