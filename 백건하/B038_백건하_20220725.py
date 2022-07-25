import sys
input = sys.stdin.readline

n, bird = map(int, input().split())

fruit = list(map(int, input().split()))

fruit.sort()

maxi = 0
for val in fruit:
    if bird < val:
        break
    bird += 1

print(bird)