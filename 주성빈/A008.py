s_num = int(input())

total = []
for i in range(s_num):
  num = list(map(int, input().split()))
  average = sum(num[1:])/num[0]
  upper_count = 0
  for score in num[1:]:
    if score > average:
      upper_count += 1
  r = upper_count/num[0] * 100
  total.append(f'{r:.3f}%')

for i in range(s_num):
  print(total[i])
