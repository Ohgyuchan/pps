import sys
input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))

count = 0
for idx in range(n):
    if l[idx] == 1:
        l[idx] = 0
        if idx+1 < n:
            l[idx+1] = 1 - l[idx+1]
            if idx+2 < n:
                l[idx+2] = 1 - l[idx+2]
        count += 1

print(count)