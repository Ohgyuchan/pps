import sys
n = int(input())
def gcd(a, b):
  while b != 0:
    r = a % b
    a = b
    b = r
  return a


for i in range(n):
  a, b = map(int, sys.stdin.readline().split())
  print(int(a*b/gcd(a, b)))
