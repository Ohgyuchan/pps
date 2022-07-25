a = [0] * 8

for i in range(8) :
    a[i] = int(input())
    
b = sorted(a, reverse=True)

print(sum(b[:5]))
answer = [str(a.index(b[i]) + 1) for i in range(5) ]
print(' '.join(sorted(answer)))