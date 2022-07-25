import sys
input = sys.stdin.readline

l = input().rstrip().split('-')

answer = 0
for idx, one in enumerate(l):
    one_l = list(map(int, one.split('+')))

    if idx == 0:
        for num in one_l:
            answer += num
    else:
        for num in one_l:
            answer -= num

print(answer)