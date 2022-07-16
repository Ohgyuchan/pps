import sys
n, k = sys.stdin.readline().split()
k = int(k)
n = int(n)
arr = [i for i in range(1, n+1)]

print("<", end='')
cnt = 0

while len(arr) > 1:
  cnt += k
  if cnt > len(arr):
    cnt %= len(arr)
    if cnt == 0:
      cnt += len(arr)
  cnt -= 1
  print(str(arr.pop(cnt)), end = ', ')
print("{}>".format(str(arr.pop())))
