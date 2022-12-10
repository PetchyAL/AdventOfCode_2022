from numpy import prod
with open("input.txt") as text_file:
  forest = text_file.read().strip().split('\n')
  forest = [list(r.strip()) for r in forest]

def get_score(lst, t):
  tree_count = 0
  for n in lst:
    tree_count += 1
    if n >= int(t): break
  return tree_count

def solve(forest, rlen, clen):
  visible_count = 0
  scenic_scores = list()
  for row in range(rlen):
    for col in range(clen):
      #Get all directions
      left = list(map(int, forest[row][:col]))
      right = list(map(int, forest[row][col+1:]))
      up = [int(c[col]) for c in forest[:row]]
      down = [int(c[col]) for c in forest[row+1:]]
      #Part 1
      if (all(n < int(forest[row][col]) for n in left) or
          all(n < int(forest[row][col]) for n in right) or
          all(n < int(forest[row][col]) for n in up) or
          all(n < int(forest[row][col]) for n in down)): visible_count += 1
      #Part 2
      scores = [get_score(reversed(left), forest[row][col]),
                get_score(right, forest[row][col]),
                get_score(reversed(up), forest[row][col]),
                get_score(down, forest[row][col])]
      scenic_scores.append(prod(scores))
  return visible_count, max(scenic_scores)
      
part_one, part_two = solve(forest, len(forest[0]), len(forest))
print(part_one) #Part 1 result
print(part_two) #Part 2 result
