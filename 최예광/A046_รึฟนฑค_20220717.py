N = int(input())
letters = [0]*26
for i in range(N):
    tmp = input()
    letters[ord(tmp[0])-97]+=1 

ans=[]
chrans=[]
for i in range(len(letters)):
    if letters[i] >= 5:
        ans.append(i)
        
if len(ans) == 0:
    print('PREDAJA')
else:
    for j in range(len(ans)):
        chrans.append(chr(ans[j]+97))
    print(''.join(chrans))
    