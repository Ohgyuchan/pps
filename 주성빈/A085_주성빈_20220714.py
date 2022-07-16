n = int(input())

def sum_num(inputs):
  fin = 0
  for i in inputs:
    if i.isdigit():
      fin += int(i)
  return fin

ans = []
for i in range(n):
  temp = input()
  ans.append(temp)

ans.sort(key = lambda x : (len(x), sum_num(x), x))
for i in ans:
  print(i)
