n = int(input())
num = 2

while num <= n:
  if n % num == 0:
    print(num)
    n /= num
  else:
    num += 1
