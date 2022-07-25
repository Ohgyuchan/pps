def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


n = int(input())
connects_count = int(input())


graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


for _ in range(connects_count):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


dfs(1)


print(visited.count(True)-1)