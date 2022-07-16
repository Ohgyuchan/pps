import sys
arr = []
idx = []
for i in range(8):
  arr.append(int(sys.stdin.readline()))

score_sort = sorted(arr, reverse=True)
final = []
for i in range(5):
  final.append(score_sort[i])

sum = 0
for i in final:
  sum += i
  idx.append(arr.index(i))
print(sum)
idx_sort = sorted(idx)
for i in idx_sort:
  print(i + 1, end=' ')
