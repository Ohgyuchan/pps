def solution(s):
    
    new_s = ''
    
    for idx, one in enumerate(s):
        if idx == 0:
            new_s += one.upper()
        else:
            if s[idx-1] == ' ':
                new_s += one.upper()
            else:
                new_s += one.lower()
    
    return new_s