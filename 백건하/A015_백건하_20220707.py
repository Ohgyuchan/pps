nums = list(map(int, input().split()))

summ = 0
for num in nums:
	summ += num * num

answer = summ % 10
print(answer)