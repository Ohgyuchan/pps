N = int(input())
count = N

for i in range(N):
    s = input()
    for j in range(0, len(s)-1):
        if s[j] == s[j+1]:
            pass
        elif s[j] in s[j+1:]:
            count -= 1
            break

print(count)