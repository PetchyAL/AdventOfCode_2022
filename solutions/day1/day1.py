with open('input.txt') as text_file:
  calorie_list = text_file.read().split('\n\n')
  totals = []

  for cals in calorie_list:
    totals.append(sum(map(int,cals.strip().split('\n'))))
  totals.sort()

print(totals[-1]) #Part 1 result
print(sum(totals[-3:])) #Part 2 result
