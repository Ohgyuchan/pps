# 끊어진 기타줄의 개수 N, 기타줄 브랜드 개수 M
import sys

n, m = map(int, sys.stdin.readline().split())
minimum = []
pk_list = []
one_list = []
for i in range(m):
  pk, one = map(int, sys.stdin.readline().split())
  pk_list.append(pk)
  one_list.append(one)

pk_min = min(pk_list)
one_min = min(one_list)

if pk_min < one_min * 6:
  if pk_min < (n%6)*one_min:
    print((n//6) * pk_min + pk_min)
  else:
    print((n//6) * pk_min + (n%6) * one_min)

else:
  print(n * one_min)
