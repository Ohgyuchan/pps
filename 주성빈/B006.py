from collections import deque

n, v, s = map(int,input().split())
# n 은 정점
# v 는 간선
# s 는 시작정점

arr = [[0] * (n+1) for i in range(n+1)]

for i in range(v):
  a, b = map(int, input().split())
  arr[a][b] = 1
  arr[b][a] = 1

# DFS
def dfs(s, arr_dfs=[]):
  arr_dfs.append(s)
  print(s, end=' ')

  for j in range(len(arr[s])):
    if arr[s][j] == 1 and (j not in arr_dfs):
      dfs(j, arr_dfs)
j = 0
# BFS
def bfs(s):
  arr_bfs = [s]
  queue = deque()
  queue.append(s)

  while queue:
    w = queue.popleft()
    print(w, end=' ')

    for j in range(len(arr[s])):
      if arr[w][j] == 1 and (j not in arr_bfs):
        arr_bfs.append(j)
        queue.append(j)

dfs(s)
print()
bfs(s)
