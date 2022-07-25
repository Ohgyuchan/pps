a = int(input())
b = int(input())
c = int(input())

counts = [0] * 10

multi = a * b * c

multi_list = list(map(int, str(multi)))

for num in multi_list:
	counts[num] += 1

for count in counts:
    print(count)