#Just a fun little extra:
#Python script to recreate the elf's file system from input
#All file sizes being the correct num of bytes
from string import digits
import os
with open("input.txt") as text_file:
  data = text_file.read().strip()
crnt_dir = [] #Current directory path/structure

for line in data.split('\n'):
  ln = line.strip().split(' ')
  #Changing current directory
  if ln[1] == 'cd':
    if ln[2] == '/':
      for _ in range(len(crnt_dir)):
        os.chdir('..')
        crnt_dir.pop()
    elif ln[2] == '..':
      os.chdir('..')
      crnt_dir.pop()
    else: 
      os.chdir(ln[2])
      crnt_dir.append(ln[2])

  #Create directory if doesn't exist
  elif ln[0] == 'dir':
    if not os.path.isfile(ln[1]):
        os.mkdir(ln[1])

  #Create file of correct size if doesn't exist
  elif ln[0][0] in digits:
    if not os.path.isfile(ln[1]):
        with open(ln[1], 'wb') as f:
            f.seek(int(ln[0])-1)
            f.write(b'\0')