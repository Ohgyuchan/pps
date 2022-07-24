import sys
input = sys.stdin.readline

a = input()

arr = []
for i in a :
    arr.append(i)

for i in sorted(arr, reverse=True) :
    print(i, end='')