import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n) :
    [x, y] = map(int, input().split())
    array.append([x, y])

array = sorted(array)

for i in range(n) :
    print(array[i][0], array[i][1])