order = list(map(int, input().split()))
length = len(order)

before = order[0]
asc = 1
desc = 1
for one in order[1:]:
        if one >= before:
                asc += 1
        
        if one <= before:
                desc += 1
        before = one

if asc == length:
	print('ascending')
elif desc == length:
	print('descending')
else:
	print('mixed')
