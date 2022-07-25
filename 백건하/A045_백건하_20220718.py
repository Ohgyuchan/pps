l = list(input().upper())

dic = {}

for one in l:
    if one not in dic:
        dic[one] = 1
    else:
        dic[one] += 1

maxi = max(dic.values())

count = 0
for key, val in dic.items():
    if val == maxi:
        count += 1
        max_key = key

if count == 1:
    print(max_key)
else:
    print('?')
