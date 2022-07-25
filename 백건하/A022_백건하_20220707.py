import sys
input = sys.stdin.readline

length = int(input())

seconds = list(map(int, input().split()))

Y = 0
M = 0
for second in seconds:
	Y += 10 * (1 + second // 30)
	M += 15 * (1 + second // 60)

if Y > M:
	print(f'M {M}')
elif M > Y:
	print(f'Y {Y}')
else:
	print(f'Y M {Y}')