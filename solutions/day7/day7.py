from string import digits
with open("input.txt") as text_file:
  data = text_file.read().strip()

dir_sizes = dict() #Keeps a size value for each directory
checked_f = dict() #Which directories and files were already checked
crnt_dir = [] #Current directory path/structure

for line in data.split('\n'):
  ln = line.strip().split(' ')
  #Changing current directory
  if ln[1] == 'cd':
    if ln[2] == '/':
      try: crnt_dir = [crnt_dir[0]]
      except: crnt_dir.append(ln[2])
    elif ln[2] == '..':
      crnt_dir.pop()
    else: crnt_dir.append(ln[2])

  #Get file sizes
  elif ln[0][0] in digits:
    dir_str = '\\'.join(crnt_dir)
    if dir_str not in checked_f: checked_f[dir_str] = []
    #Check if file size was already added
    if ln[1] not in checked_f[dir_str]:
      checked_f[dir_str].append(ln[1])
      for f in range(len(crnt_dir)+1):
        if '\\'.join(crnt_dir[:f]) not in dir_sizes.keys():
          dir_sizes['\\'.join(crnt_dir[:f])] = 0
        dir_sizes['\\'.join(crnt_dir[:f])] += int(ln[0])
    
#Part 1
print(sum(x for x in dir_sizes.values() if x <= 100000))

#Part 2
space_needed = 30000000-(70000000-max(dir_sizes.values()))
print(min(x for x in dir_sizes.values() if x >= space_needed))
