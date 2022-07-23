for i in range(int(input())):
  n = int(input())
  cnt = 1
  for j in range(n-1):
    cnt = cnt * 2 + 1
  print(cnt)
