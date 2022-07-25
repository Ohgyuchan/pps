import sys
input = sys.stdin.readline

n, k = map(int, input().split())

num = [i for i in range(1, n+1)]

idx = -1
answer = []
for _ in range(n):
    idx += k
    idx %= len(num)

    answer.append(num.pop(idx))
    idx -= 1

print('<', end='')
for idx, one in enumerate(answer):
    print(one, end='')
    if idx != len(answer)-1:
        print(', ', end='')
print('>')