ans = []
cnt = 0
for i in range(10):
  n = int(input())
  if n % 42 not in ans:
    cnt += 1
    ans.append(n%42)

print(cnt)
