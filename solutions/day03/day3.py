from string import ascii_letters
with open('input.txt') as text_file:
  rucksacks = text_file.read().strip().split('\n')
  values = dict(zip(ascii_letters, range(1,53)))

def part_one():
  sum_priority = 0
  for sack in rucksacks:
    comp_a = set(sack[:len(sack)//2])
    comp_b = set(sack[len(sack)//2:])
    for c in comp_a.intersection(comp_b): sum_priority += values[c]
  return sum_priority

def part_two():
  sum_priority = 0
  while len(rucksacks) > 0:
    sum_priority += values[set(rucksacks[0]).intersection(set(rucksacks[1]),set(rucksacks[2])).pop()]
    del rucksacks[:3]
  return(sum_priority)

print(part_one())
print(part_two())
