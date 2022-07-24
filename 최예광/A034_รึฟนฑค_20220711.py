li=[]
for _ in range(10):
    tmp = int(input())%42
    li.append(tmp)
    
print(len(set(li)))
    