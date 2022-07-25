n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

answer = 0
for one in coin:
    answer += k // one
    k = k % one

print(answer)