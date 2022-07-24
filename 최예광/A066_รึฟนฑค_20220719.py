n = int(input())
nlist=[]
for i in str(n):
    nlist.append(i)
nlist.sort(reverse=True)

print("".join(nlist))