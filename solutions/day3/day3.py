import string
text_file = open('input.txt')
rucksacks = text_file.read().strip().split('\n')

values = dict()
for index, lower_case in enumerate(string.ascii_lowercase):
  values[lower_case] = index + 1
for index, upper_case in enumerate(string.ascii_uppercase):
  values[upper_case] = index + 27

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