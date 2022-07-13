remainders = [0] * 10

for i in range(10) :
    num = int(input())
    remainders[i] = num % 42

remainders = set(remainders) # 중복 제거

print(len(remainders))