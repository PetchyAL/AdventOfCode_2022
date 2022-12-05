from string import ascii_uppercase
import copy

def prep_cargo(cargo):
  prepped_cargo = [ [] for _ in range(int(cargo[-1].strip()[-1])) ]
  for row in cargo:
    for c in range(len(row)):
      if row[c] in ascii_uppercase:
        prepped_cargo[c//4].append(row[c])
  return prepped_cargo

with open("input.txt") as text_file:
  cargo, instructions = text_file.read().strip().split('\n\n')
cargo = prep_cargo(cargo.split('\n'))
cargo_one = copy.deepcopy(cargo)
cargo_two = copy.deepcopy(cargo)

for instruction in instructions.split('\n'):
  i = instruction.strip().split(' ')
  n, fr, to = int(i[1]), int(i[3]), int(i[5])
  for _ in range(n): #Part 1
    cargo_one[to-1].insert(0, cargo_one[fr-1].pop(0))
  for num in reversed(range(n)): #Part 2
    cargo_two[to-1].insert(0, cargo_two[fr-1].pop(num))

print(''.join(list(stack[0] for stack in cargo_one))) #Part 1 result
print(''.join(list(stack[0] for stack in cargo_two))) #Part 2 result
