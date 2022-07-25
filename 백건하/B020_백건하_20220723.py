'''
dfs 하면서 이어붙이는데 6 count -> set에 add
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(r_, c_, count, number):
    if count == 6:
        s.add(number)
        return
    
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    for i in range(4):
        new_r = r_ + dr[i]
        new_c = c_ + dc[i]

        if new_r>=0 and new_r<5 and new_c>=0 and new_c<5:
            dfs(new_r, new_c, count+1, number+mapp[new_r][new_c])

s = set()

mapp = []
for _ in range(5):
    mapp.append(list(input().split()))

for r in range(5):
    for c in range(5):
        dfs(r, c, 1, mapp[r][c])

print(len(s))
