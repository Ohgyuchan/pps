Ycost = 0
Mcost = 0
N = int(input())
history = list(map(int, input().split()))

for num in history:
    Ycost += (num//30) * 10 + 10
    Mcost += (num//60) * 15 + 15

if Mcost < Ycost:
    print("M",Mcost)
elif Ycost < Mcost:
    print("Y",Ycost)
else:
    print("Y M", Mcost)