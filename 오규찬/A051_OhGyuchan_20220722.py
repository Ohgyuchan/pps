num = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()
time = 0
for i in a :
    for idx in range(9) :
        if i in num[idx] :
            time += (idx + 2)

print(time)