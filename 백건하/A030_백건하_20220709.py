n, bad = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

before_bad = bad
before_good = 1 - before_bad

for _ in range(n):
	good = before_good * gg + before_bad * bg
	bad = 1 - good
	before_good = good
	before_bad = bad

print(round(1000 * good))
print(round(1000 * bad))
