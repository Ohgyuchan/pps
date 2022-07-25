import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    l = input().split()

    cont = l[0]
    if cont == 'push':
        stack.append(l[1])
    elif cont == 'pop':
        if stack:
            num = stack.pop()
            print(num)
        else:
            print(-1)
    elif cont == 'size':
        print(len(stack))
    elif cont == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif cont == 'top':
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)
