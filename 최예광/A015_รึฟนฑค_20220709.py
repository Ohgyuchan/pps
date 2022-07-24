n = list(map(int,input().split()))
sum = 0
for i in range(5):
    tmp = n[i]*n[i]
    sum += tmp

print(sum%10)