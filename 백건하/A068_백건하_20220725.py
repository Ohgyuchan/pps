import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

queue = deque([])
for _ in range(n):
    l = input().split()

    ctrl = l[0]

    if ctrl == 'push':
        queue.append(l[1])
    elif ctrl == 'pop':
        if queue:
            num = queue.popleft()
            print(num)
        else:
            print(-1)
    elif ctrl == 'size':
        print(len(queue))
    elif ctrl == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif ctrl == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif ctrl == 'back':
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)