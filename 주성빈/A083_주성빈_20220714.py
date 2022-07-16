import sys
n = int(sys.stdin.readline())
unique_number = []

temp = list(map(int, sys.stdin.readline().split()))
if n == len(temp):
  for j in range(n):
    if temp[j] not in unique_number:
      unique_number.append(temp[j])

  unique_number.sort()
  
  for i in range(len(unique_number)):
    print(unique_number[i], end=' ')
