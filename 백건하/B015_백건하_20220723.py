import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(idx):
    visited[idx] = True

    step = [jump[idx], -jump[idx]]

    for i in range(2):
        new_idx = idx + step[i]
        if new_idx>=0 and new_idx<n:
            if not visited[new_idx]:
                dfs(new_idx)


n = int(input())
jump = list(map(int, input().split()))
now = int(input()) - 1

visited = [False for _ in range(n)]

dfs(now)

print(visited.count(True))