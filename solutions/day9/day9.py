with open("input.txt") as text_file:
  instructions = text_file.read().strip().split('\n')

def adjacent(lst1, lst2):
  positions = [[lst1[0]+1, lst1[1]+1], [lst1[0]-1, lst1[1]-1],
               [lst1[0]+1, lst1[1]-1], [lst1[0]-1, lst1[1]+1],
               [lst1[0]+1, lst1[1]], [lst1[0]-1, lst1[1]],
               [lst1[0], lst1[1]-1], [lst1[0], lst1[1]+1]]
  return True if lst2 in positions else False

def move(dir, lst, vst):
  if dir == 'R': lst[-1][1] += 1
  elif dir == 'L': lst[-1][1] -= 1
  elif dir == 'D': lst[-1][0] += 1
  else: lst[-1][0] -= 1

  for n in reversed(range(len(lst)-1)):
    if not adjacent(lst[n+1], lst[n]):
      lst[n][1] += 1 if lst[n][1] < lst[n+1][1] else 0
      lst[n][1] -= 1 if lst[n][1] > lst[n+1][1] else 0
      lst[n][0] += 1 if lst[n][0] < lst[n+1][0] else 0
      lst[n][0] -= 1 if lst[n][0] > lst[n+1][0] else 0
  if lst[0] not in vst:
    vst.append(lst[0].copy())
  return lst, vst

knots_one = [[0,0] for _ in range(2)]
knots_two = [[0,0] for _ in range(10)]
visits_one, visits_two = list(), list()
for inst in instructions:
  i = inst.split(' ')
  for _ in range(int(i[1])):
    knots_one, visits_one = move(i[0], knots_one, visits_one)
    knots_two, visits_two = move(i[0], knots_two, visits_two)

print(len(visits_one)) #Part 1 result
print(len(visits_two)) #Part 2 result