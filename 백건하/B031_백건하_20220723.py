import sys
input = sys.stdin.readline


from_, to_ = map(int, input().split())
n = int(input())

cango = []
for _ in range(n):
    cango.append(int(input()))

mini = abs(to_ - from_)

for one in cango:
    candi = abs(to_ - one) + 1
    if candi < mini:
        mini = candi

print(mini)