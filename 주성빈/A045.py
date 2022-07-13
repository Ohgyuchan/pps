string = input().upper()
a = [] # unique
cnt = []
for i in range(len(string)):
  if string[i] not in a:
    a.append(string[i])

for i in range(len(a)):
  cnt.append(string.count(a[i]))

if cnt.count(max(cnt)) > 1:
  print('?')
else:
  print(a[cnt.index(max(cnt))])
