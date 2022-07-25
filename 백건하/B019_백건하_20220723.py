import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(r_, c_, isRG):
    visited[r_][c_] = True

    now = mapp[r_][c_]

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    for i in range(4):
        new_r = r_ + dr[i]
        new_c = c_ + dc[i]

        if new_r>=0 and new_r<n and new_c>=0 and new_c<n:
            if not visited[new_r][new_c]:
                nextt = mapp[new_r][new_c]
                if now==nextt or ( isRG and ((now=='R' and nextt=='G') or (now=='G' and nextt=='R')) ):
                    dfs(new_r, new_c, isRG)


n = int(input())

mapp = []
for _ in range(n):
    mapp.append(list(input().rstrip()))

visited = [[False for _ in range(n)] for _ in range(n)]

count = 0
for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            dfs(r, c, False)
            count += 1
print(count)

visited = [[False for _ in range(n)] for _ in range(n)]

count = 0
for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            dfs(r, c, True)
            count += 1
print(count)
