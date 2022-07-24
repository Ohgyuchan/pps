li = []
for _ in range(8):
    li.append(int(input()))

sum = 0
idx = []
for i in range(5):
    idx.append(li.index(max(li))+1)
    sum += max(li)
    li[li.index(max(li))] = 0
idx.sort()
print(sum)
for n in idx:
    print(n, end = " ")
