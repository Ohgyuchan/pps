n = int(input())
ans = []
for i in range(n):
  line = list(map(str, input().split()))
  sum = float(line[0])
  for j in range(1, len(line)):
    if line[j] == '@':
      sum *= 3
    elif line[j] == '%':
      sum += 5
    else:
      sum -= 7
  ans.append(sum)

for i in range(n):
  print("{:.2f}".format(ans[i]))
