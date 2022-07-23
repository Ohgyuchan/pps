n = int(input())

def dp(t):
  if t == 1:
    return 1
  elif t == 2:
    return 2
  elif t == 3:
    return 4
  else:
    return dp(t-1) + dp(t-2) + dp(t-3)

for i in range(n):
  k = int(input())
  print(dp(k))
