import sys
input = sys.stdin.readline

l = list(input())
l.pop()
l.sort(reverse = True)

s = ''.join(l)
print(s)
