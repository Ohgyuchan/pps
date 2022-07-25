import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(r_, c_):
    visited[r_][c_] = True

    dr = [0, 0, 1, -1, 1, 1, -1, -1]
    dc = [1, -1, 0, 0, 1, -1, 1, -1]

    for i in range(8):
        new_r = r_ + dr[i]
        new_c = c_ + dc[i]

        if new_r>=0 and new_r<row and new_c>=0 and new_c<col:
            if mapp[new_r][new_c]==1 and not visited[new_r][new_c]:
                dfs(new_r, new_c)


while True:
    col, row = map(int, input().split())
    if col==0 and row==0:
        break

    mapp = []
    for _ in range(row):
        mapp.append(list(map(int, input().split())))

    visited = [[False for _ in range(col)] for _ in range(row)]

    count = 0
    for r in range(row):
        for c in range(col):
            if mapp[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                count += 1

    print(count)
