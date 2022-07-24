N, mood = map(int, input().split())
m = list(map(float, input().split()))

if mood == 0:
    p = m[0]
else:
    p = m[2]
    
if N > 1:
    for i in range(N)[1:]:
        p = p*m[0] + (1-p)*m[2]

print(round(p*1000))
print(round((1-p)*1000))