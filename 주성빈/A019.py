a = int(input())
b = int(input())
c = int(input())
arr = [0] * 10

n = a*b*c
tot = list(map(int, str(n)))

for i in range(len(tot)):
  arr[tot[i]] += 1

for i in range(0, 10):
  print(arr[i])
