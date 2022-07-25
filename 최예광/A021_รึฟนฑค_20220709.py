A = int(input())
B = int(input())
C = int(input())
mul = A * B * C
mul_list = list(map(int,str(mul)))

num = [0]*10

for i in mul_list:
    num[i] += 1
for j in num:
    print(j)

    
    