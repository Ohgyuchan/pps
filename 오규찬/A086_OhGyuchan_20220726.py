m, n = map(int, input().split())

nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
a = []

for i in range(m, n + 1) :
    b = [nums[int(c)] for c in str(i)]
    num = ' '.join(b)
    a.append(num)

a.sort()

for i in range(n - m + 1) :
    num = a[i].split()
    if len(num) == 1 :
        print(nums.index(num[0]), end= ' ')
    else :
        print(nums.index(num[0]), end= '')
        print(nums.index(num[1]), end= ' ')
    if (i + 1) % 10 == 0 :
        print()