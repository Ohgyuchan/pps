score = 0
w = 1
N = int(input())
for i in range(N):
    oxes = input()
    for c in oxes:
        if c == 'O':
            score += w
            w += 1
        elif c == 'X':
            w = 1
    print(score)
    score = 0
    w = 1