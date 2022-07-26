N = int(input())
a = list(map(int, input().split()))

for i in sorted(list(set(a))):
    print(i, end = ' ')