n = int(input()) # the number of test
ans = []
for i in range(n):
  f = int(input())
  h = int(input())
  f_0 = [x for x in range(1, h+1)] # 0 floor
  for k in range(f):
    for l in range(1, h):
      f_0[l] += f_0[l-1]
  ans.append(f_0[-1])

for i in range(n):
  print(ans[i])
