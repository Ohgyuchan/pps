import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

# from_c & from_w -> to_c, to_w 를 받아
# return new from_w, to_w
def flow(from_c, from_w, to_c, to_w):
    if from_w + to_w <= to_c:
        to_w += from_w
        from_w = 0
    else:
        from_w = from_w + to_w - to_c
        to_w = to_c

    return from_w, to_w

def dfs(A_w, B_w, C_w):
    visited[A_w][B_w][C_w] = True

    new_A_w, new_B_w = flow(A_c, A_w, B_c, B_w)
    if not visited[new_A_w][new_B_w][C_w]:
        dfs(new_A_w, new_B_w, C_w)

    new_A_w, new_C_w = flow(A_c, A_w, C_c, C_w)
    if not visited[new_A_w][B_w][new_C_w]:
        dfs(new_A_w, B_w, new_C_w)

    new_B_w, new_A_w = flow(B_c, B_w, A_c, A_w)
    if not visited[new_A_w][new_B_w][C_w]:
        dfs(new_A_w, new_B_w, C_w)

    new_B_w, new_C_w = flow(B_c, B_w, C_c, C_w)
    if not visited[A_w][new_B_w][new_C_w]:
        dfs(A_w, new_B_w, new_C_w)

    new_C_w, new_A_w = flow(C_c, C_w, A_c, A_w)
    if not visited[new_A_w][B_w][new_C_w]:
        dfs(new_A_w, B_w, new_C_w)

    new_C_w, new_B_w = flow(C_c, C_w, B_c, B_w)
    if not visited[A_w][new_B_w][new_C_w]:
        dfs(A_w, new_B_w, new_C_w)
    
    
A_c, B_c, C_c = map(int, input().split())
A_w, B_w, C_w = 0, 0, C_c

visited = [[[False for i in range(C_c+1)] for j in range(B_c+1)] for k in range(A_c+1)]

dfs(A_w, B_w, C_w)

answer = []
for j in range(B_c+1):
    for k in range(C_c+1):
        if visited[0][j][k]:
            answer.append(k)

answer.sort()
for one in answer:
    print(one)