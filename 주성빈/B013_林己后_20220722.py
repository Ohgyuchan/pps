import sys
from collections import deque

def sv(x, y):
  if not visited[x][y]:
    visited[x][y] = True
    ans.append((x, y))

def bfs():
  while ans:
    al, bl = ans.popleft()
    cl = c - al - bl

    if al == 0:
      temp.append(cl)

    water = min(al, b-bl)
    sv(al - water, bl + water)

    water = min(al, c-cl)
    sv(al - water, bl)

    water = min(bl, a-al)
    sv(al + water, bl - water)

    water = min(bl, c-cl)
    sv(al, bl - water)

    water = min(cl, a-al)
    sv(al + water, bl)

    water = min(cl, b-bl)
    sv(al, bl + water)

a, b, c = map(int, sys.stdin.readline().split())

ans = deque()
ans.append((0, 0))

visited = [[False] * 201 for i in range(201)]
visited[0][0] = True

temp = []
bfs()

temp.sort()
print(*temp)
