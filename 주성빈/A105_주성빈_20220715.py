n = int(input())
num_arr = []

num = 0
cnt = 0

while cnt < n:
  num += 1
  cnt += num

cnt -= num

if num % 2 == 0:
  temp_1 = n - cnt
  temp_2 = num - temp_1 + 1
else:
  temp_1 = num - (n - cnt) + 1
  temp_2 = n - cnt

print(f'{temp_1}/{temp_2}')
