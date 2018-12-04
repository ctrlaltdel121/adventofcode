# Part 1 ;)
with open('1.input') as f: exec('print(\'Part 1:\','+''.join(f.read().replace('\n', ''))+")")
    

# part 2
with open('1.input') as f:
    input = f.readlines()

val = 0
vals = set()
while True:
  for x in input:
    val += int(x)
    if val in vals:
        print("Part 2:", val)
        exit()
    vals.add(val)