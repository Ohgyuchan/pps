n = int(input())

for i in range(n) :
    test = input()
    score = 0
    repeat = 0
    for t in test :
        if t == 'O' :
            repeat += 1
            score += repeat
        else :
            repeat = 0
    print(score)