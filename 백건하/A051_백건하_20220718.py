l = list(input())

# 65 ~ 90
# 67 70 73 76 79 83 86 90
# 65 ~ 67 -> 9 10 11 -> 3
# num -= 56
time = 0
for one in l:
    num = ord(one)
    if num >= 90:
        num -= 2
    elif num >= 83:
        num -= 1

    num -= 56
    time += num//3
    
print(time)
