num = input()
num = [int(i) for i in num]

order_num = sorted(num, reverse=True)

for i in order_num:
  print(i, end="")
