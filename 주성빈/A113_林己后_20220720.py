# 정점의 개수 N, 간선의 개수 M

import sys
sys.setrecursionlimit(10**7)
n, m = map(int, sys.stdin.readline().split())
graph = [[0] for i in range(n+1)]
visit = [False] * (n+1)
cnt = 0

def dfs(v):
  visit[v] = True
  for i in graph[v]:
    if visit[i] == False:
      visit[i] = True
      dfs(i)

for i in range(m):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(1, n+1):
  if visit[i] == False:
    cnt += 1
    dfs(i)

print(cnt)
