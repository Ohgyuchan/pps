n = int(input())
arr = list(map(int, input().split()))
sum_y = 0
sum_m = 0
for i in range(n):
  sum_y += ((arr[i]+30)//30)*10
  sum_m += ((arr[i]+60)//60)*15

if sum_y < sum_m:
  print('Y', sum_y, sep=' ')

elif sum_y > sum_m:
  print('M', sum_m, sep=' ')

else:
  print('Y', 'M', sum_y, sep=' ')
