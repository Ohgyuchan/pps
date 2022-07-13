inputs = [0] * 5
inputs[0] = list(map(int, input().split()))
inputs[1] = list(map(int, input().split()))
inputs[2] = list(map(int, input().split()))
inputs[3] = list(map(int, input().split()))
inputs[4] = list(map(int, input().split()))

winnerScore = 0
winnerIndex = 0
for i in range(5) :
    tmp = sum(inputs[i])
    if tmp > winnerScore :
        winnerScore = tmp
        winnerIndex = i + 1

print(winnerIndex, winnerScore)