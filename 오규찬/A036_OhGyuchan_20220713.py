import sys

#inf = open('input.txt');
inf = sys.stdin 
T = inf.readline();
for t in range(0, int(T)):
	
    int(input())
    
    nums = list(map(int,input().split()))
    s = set()
    for i in nums :
        if i in s :
            s.remove(i) # 중복이면 없앰.
        else :
            s.add(i)
    Answer = -1
    
    for i in s :
        if Answer == -1 :
            Answer = i
        else:
            Answer = Answer ^ i
    
    # Print the answer to standard output(screen).
    print('Case #%d' %(int(t)+1))
    print(Answer)
inf.close()
