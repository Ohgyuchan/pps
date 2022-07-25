import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([])
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif order[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
            
    
    