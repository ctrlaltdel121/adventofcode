import re

with open('4.input') as f:
    input = f.read()

inputSpl = input.split('\n\n')

eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def determine(pp, part2):
    hasFields = 'byr' in pp and 'iyr' in pp and 'eyr' in pp and 'hgt' in pp and 'hcl' in pp and 'ecl' in pp and 'pid' in pp
    if not hasFields:
        return False
    elif not part2:
        return True

    fields = pp.split()
    for f in fields:
        fieldValid = False
        kval = f.split(':')
        if kval[0] == "byr" and int(kval[1]) >= 1920 and int(kval[1]) <= 2002:
            fieldValid = True
        elif kval[0] == "iyr" and int(kval[1]) >= 2010 and int(kval[1]) <= 2020:
            fieldValid = True
        elif kval[0] == "eyr" and int(kval[1]) >= 2020 and int(kval[1]) <= 2030:
            fieldValid = True
        elif kval[0] == "hgt":
            if kval[1].rfind("in") != -1:
                if int(kval[1][:kval[1].rfind("in")]) >= 59 and int(kval[1][:kval[1].rfind("in")]) <= 76:
                    fieldValid = True
            elif kval[1].rfind("cm") != -1:
                if int(kval[1][: kval[1].rfind("cm")]) >= 150 and int(kval[1][: kval[1].rfind("cm")]) <= 193:
                    fieldValid = True
        elif kval[0] == "hcl" and re.match(r'^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$', kval[1]):
            fieldValid = True
        elif kval[0] == "ecl" and kval[1] in eyeColors:
            fieldValid = True
        elif kval[0] == "pid" and re.match(r'^\d\d\d\d\d\d\d\d\d$', kval[1]):
            fieldValid = True
        elif kval[0] == "cid":
            fieldValid = True
        if not fieldValid:
            return False
    return True


p1Count = 0
p2Count = 0

for pp in inputSpl:
    if determine(pp, False):
        p1Count += 1
    if determine(pp, True):
        p2Count += 1

print("Part 1:", p1Count)
print("Part 2:", p2Count)
