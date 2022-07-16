import sys
n = int(sys.stdin.readline())
for i in range(n):
  test = list(map(int, sys.stdin.readline().split()))
  test = sorted(test, reverse=True)
  print(test[2])
