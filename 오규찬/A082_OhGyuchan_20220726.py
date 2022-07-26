n = int(input())

a = []
for _ in range(n):
    (age, name) = input().split()
    a.append((int(age), name))


b = sorted(a, key=lambda age: age[0])

for i in b:
    print(i[0], i[1])   