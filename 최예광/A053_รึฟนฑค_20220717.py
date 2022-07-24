import sys
N = int(sys.stdin.readline())
st = []
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        st.append(order[1])
    elif order[0] == 'pop':
        if len(st) != 0:
            print(st[-1])
            st.pop()
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(st))
    elif order[0] == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(st) != 0:
            print(st[-1])
        else:
            print(-1)