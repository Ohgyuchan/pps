n = int(input())
ans = []
for i in range(n):
  num = int(input())
  if num == 0:
    del ans[-1]
  else:
    ans.append(num)

print(sum(ans))
