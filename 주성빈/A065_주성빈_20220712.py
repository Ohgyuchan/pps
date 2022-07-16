import sys
n = int(sys.stdin.readline())
graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))
graph.sort()
for i in range(n):
  print(graph[i][0], graph[i][1])
