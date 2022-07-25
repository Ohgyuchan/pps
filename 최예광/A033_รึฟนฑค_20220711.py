v=[]
for _ in range(5):
    v.append(sum(list(map(int,input().split()))))

print(v.index(max(v))+1,max(v))