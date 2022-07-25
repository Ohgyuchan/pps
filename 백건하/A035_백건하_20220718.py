T = int(input())

for _ in range(T):
    l = list(input().split())
    num = float(l[0])
    op = l[1:]

    for one in op:
        if one == '@':
            num *= 3
        elif one == '%':
            num += 5
        elif one == '#':
            num -= 7

    print(f'{num :.2f}')
