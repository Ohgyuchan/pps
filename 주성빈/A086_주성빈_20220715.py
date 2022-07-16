m, n = map(int, input().split())

dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

ans = []

for i in range(m, n+1):
  temp = ' '.join([dict[j] for j in str(i)])
  ans.append([i, temp])

ans.sort(key = lambda x:x[1])

for i in range(len(ans)):
  if i%10 == 0 and i != 0:
    print(sep = '\n')
  print(ans[i][0], end=' ')
