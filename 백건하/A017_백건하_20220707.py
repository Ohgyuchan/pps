nums = list(map(int, input()))

count = [0] * 10
for num in nums:
	count[num] += 1

count[6] = (count[6] + count[9] + 1) // 2
count[9] = 0

print(max(count))
