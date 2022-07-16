n = int(input())
for i in range(n):
  case = input()
  score = 0
  sum = 0
  for j in case:
    if j == 'O':
      score += 1
    else:
      score = 0
    sum += score
  print(sum)
