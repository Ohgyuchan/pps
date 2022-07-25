import sys
input = sys.stdin.readline

score = []
for _ in range(8):
    score.append(int(input()))

for idx, one in enumerate(score):
    score[idx] = [one, idx+1]

score.sort(key = lambda x: x[0])

summ = 0
answer_idx = []
for i in range(3, len(score)):
    val, idx = score[i]
    summ += val
    answer_idx.append(idx)

answer_idx.sort()

print(summ)
for one in answer_idx:
    print(one, end=' ')