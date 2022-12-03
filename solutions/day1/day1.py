text_file = open('input.txt')
calorie_list = text_file.read().split('\n\n')
totals = []

for cals in calorie_list:
  totals.append(sum(list(map(int,cals.strip().split('\n')))))
totals.sort()

print(totals[-1]) #Part 1 result
print(sum(totals[-3:])) #Part 2 result
