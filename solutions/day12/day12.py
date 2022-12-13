from collections import deque
with open("input.txt") as text_file:
  grid = [list(x.strip()) for x in text_file.read().strip().split('\n')]

for i, row in enumerate(grid):
  if 'S' in row: 
    srow, scol = i, row.index('S')
    grid[i][row.index('S')] = 'a'
  if 'E' in row: 
    trow, tcol = i, row.index('E')
    grid[i][row.index('E')] = 'z'

def bfs(sr, sc, tr, tc, p2):
  q = deque()
  q.append((0, sr, sc))
  vst = {(sr, sc)}
  while q:
    d, r, c = q.popleft()
    for ar, ac in [(r+1, c),(r-1, c),(r, c+1),(r, c-1)]:
      if ar < 0 or ar >= len(grid) or ac < 0 or ac >= len(grid[0]):
        continue
      if (ar, ac) in vst:
        continue
      if not p2:
        if ord(grid[ar][ac]) - ord(grid[r][c]) > 1:
          continue
        if ar == tr and ac == tc: return(d+1)
      else:
        if ord(grid[ar][ac]) - ord(grid[r][c]) < -1:
          continue
        if grid[ar][ac] == 'a': return(d+1)
      q.append((d+1, ar, ac))
      vst.add((ar, ac))

print(bfs(srow, scol, trow, tcol, False)) #Part 1 result
print(bfs(trow, tcol, None, None, True)) #Part 2 result