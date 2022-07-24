n = input()
num = [0]*10

for i in range(len(n)):
    tmp = int(n[i])
    if tmp == 6 or tmp == 9:
        if num[9] <= num[6]:
            num[9] += 1
        else:
            num[6] += 1
    else:
        num[tmp] += 1

print(max(num))
    