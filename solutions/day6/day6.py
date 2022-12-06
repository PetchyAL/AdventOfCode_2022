def marker_finder(coms, marker_len):
  for n in range(marker_len, len(coms)):
    marker_set = coms[n-marker_len:n]
    if len(set(marker_set)) == marker_len:
      return(n)

with open("input.txt") as text_file:
  coms = text_file.read().strip()

print(marker_finder(coms,4)) #Part 1 result
print(marker_finder(coms,14)) #Part 2 result
