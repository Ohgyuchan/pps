import sys
from collections import deque
n = sys.stdin.readline()
n = int(n)
q = deque()

for i in range(n):
  q.append(i+1)

while len(q) > 1:
  q.popleft()
  q.append(q.popleft())

print(q.pop())
