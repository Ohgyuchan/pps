n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse = True)

sum = 0
for i in range(n):
    tmp = A[i] * B[i]
    sum += tmp

print(sum)