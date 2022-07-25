import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(start, end):

    if start > end:
        return

    root = start
    left_start = start + 1
    right_start = end + 1

    for now in range(start+1, end+1):
        if graph[root] < graph[now]:
            right_start = now
            break

    dfs(left_start, right_start-1)
    dfs(right_start, end)
    print(graph[root])


graph = []
while True:
    try:
        graph.append(int(input()))
    except:
        break

dfs(0, len(graph)-1)
