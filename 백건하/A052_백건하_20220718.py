n = int(input())

for _ in range(n):
    l = list(input())

    O_count = 0
    score = 0
    for one in l:
        if one == 'O':
            O_count += 1
            score += O_count
        else:
            O_count = 0

    print(score)
