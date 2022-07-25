n = int(input())

count = 0
for _ in range(n):
    l = list(input())

    exists = []

    is_group = True
    for idx, one in enumerate(l):
        if one not in exists:
            exists.append(one)
        else:
            if l[idx-1] != one:
                is_group = False
                break

    if is_group:
        count += 1


print(count)
