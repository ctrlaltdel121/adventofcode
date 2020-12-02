# part 1
with open('1.input') as f:
    input = f.readlines()


addCombos = []
for i, x in enumerate(input):
  for j, y in enumerate(input[i+1:]):
    if int(x) + int(y) < 2020:
      # prework for part 2
      addCombos.append((int(x)+int(y), int(x), int(y)))
    elif int(x) + int(y) == 2020:
      print(int(x)*int(y))


# part 2
for x in addCombos:
  for y in input:
    if x[0] + int(y) == 2020:
      print(x[1]*x[2]*int(y))
      exit(0)