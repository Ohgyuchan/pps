n = list(map(int, input()))
cnt_arr = [0] * 10

for i in range(len(n)):
  if n[i] == 6 or n[i] == 9:
    cnt_arr[6] += 1
  else:
    cnt_arr[n[i]] += 1

if cnt_arr[6] % 2 == 0:
  cnt_arr[6] = cnt_arr[6] // 2
else:
  cnt_arr[6] = cnt_arr[6] // 2 + 1
  
print(max(cnt_arr))
