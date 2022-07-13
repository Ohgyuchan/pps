n = int(input())
sum = 0

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

for i in range(n):
  sum += min(a_list) * max(b_list)
  a_list.pop(a_list.index(min(a_list)))
  b_list.pop(b_list.index(max(b_list)))

print(sum)
