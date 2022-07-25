l = list(input())

# 65 ~ 90
# 65 + (x - 65 + 26 - 3) % 26
for one in l:
    print(chr(65 + (ord(one) - 65 + 26 - 3) % 26), end='')
