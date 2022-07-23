n = int(input())

for i in range(n):
  num = input()
  reverse_num = num[::-1]

  sum = str(int(num) + int(reverse_num))
  if sum == sum[::-1]:
    print("YES")
  else:
    print("NO")
