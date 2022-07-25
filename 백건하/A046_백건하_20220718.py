n = int(input())

dic = {}

for _ in range(n):
    name = input()
    first = name[0]
    if first not in dic:
        dic[first] = 1
    else:
        dic[first] += 1

if max(dic.values()) < 5:
    print("PREDAJA")
else:
    l = []
    for key, val in dic.items():
        if val >= 5:
            l.append(key)

    l.sort()
    for one in l:
        print(one, end='')
