N = int(input())
names = []

player = []
answer = []

for i in range(N) :
    name = input()
    player.append(name[0])
compare = sorted(list(set((player))))

for i in compare :
    if player.count(i) >= 5 :
        answer.append(i)
        
if len(answer) == 0 :
    print("PREDAJA")
else :
    print(''.join(answer))
