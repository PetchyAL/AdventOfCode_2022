with open("input.txt") as text_file:
  data = iter(text_file.read().strip().split('\n'))

rx, buffer = 1, 0
t_cycles = [20, 60, 100, 140, 180, 220]
cycle, n_cycle = 0, 0
sig_str = 0

crt = [['.']*40 for i in range(6)]
def check_crt(): #Update CRT each cycle
  row = cycle // 40
  col = (cycle % 40)-1
  sprite_pos = [rx-1, rx, rx+1]
  if col in sprite_pos: 
    crt[row][col] = '#'

while True: #Loop until all instructions executed
  try:
    check_crt() #Part 2
    if cycle in t_cycles: #Check target cycles
      sig_str += cycle * rx
    if cycle == n_cycle: #Add to register
      rx += buffer
      buffer = 0
    if buffer == 0: #Check if ready for next instr
      instr = next(data).strip().split(' ')
      if instr[0] == "addx":
        buffer = int(instr[1])
        n_cycle += 2
      else: n_cycle += 1
    cycle += 1 #Incr cycle
  except StopIteration: break #Exit loop when finished iterating

print(sig_str) #Part 1 result
for row in crt: #Part 2 result
  print(''.join(row))
