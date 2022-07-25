def solution(s):
    pcount = 0
    ycount = 0
    for i in range(len(s)):
        if(s[i] == 'p') or (s[i] == 'P'):
            pcount += 1
        if(s[i] == 'y') or (s[i] == 'Y'):
            ycount += 1
    
    if(pcount == ycount):
        return True
    else:
        return False