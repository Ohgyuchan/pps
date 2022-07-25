def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for next_v in graph[v]:
        if visited[next_v] == False:
            dfs(next_v)


def bfs(start_v_):
    queue = [start_v_]
    while queue:
        v = queue.pop(0)
        if visited[v] == False:
            visited[v] = True
            print(v, end=' ')
            for next_v in graph[v]:
                queue.append(next_v)


v, e, start_v = map(int, input().split())

graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, v+1):
    graph[i].sort()

dfs(start_v)
print()

visited = [False] * (v+1)

bfs(start_v)
