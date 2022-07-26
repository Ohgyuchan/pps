s = input()

a = []

for i in range(len(s)) :
    a.append(s[i:])

for i in sorted(a) :
    print(i)