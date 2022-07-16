import sys
n = int(sys.stdin.readline())
s = []
start = 0

for i in range(n):
  age, name = map(str, sys.stdin.readline().split())
  age = int(age)
  s.append((age, name))

s.sort(key = lambda x : x[0])

for i in range(n):
  print(s[i][0], s[i][1], sep=' ')
