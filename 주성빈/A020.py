ans = [[0]*4]
f, s = map(int, input().split())
ans[0] = s-f
for i in range(1,4):
  a, b = map(int, input().split())
  ans.append(ans[i-1] + b - a)

print(max(ans))
