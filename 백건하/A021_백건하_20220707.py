import sys

input = sys.stdin.readline

length = int(input())

count = 1
for i in range(length):
	num = int(input())
	count -= 1
	count += num

print(count)
