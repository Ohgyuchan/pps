l = []
for _ in range(5):
    score = sum(list(map(int, input().split())))
    l.append(score)

maxi = max(l)
maxi_num = l.index(maxi) + 1

print(maxi_num, maxi)
