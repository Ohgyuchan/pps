def first(s):
    clist = ('aeiou')
    for c in s:
        if c in clist:
            return True
    return False

def second(s):
    clist = ('aeiou')
    m = j = 0
    for c in s:
        if c in clist:
            m += 1
            j = 0
        else:
            j += 1
            m = 0
        if m == 3 or j == 3:
            return False
    return True

def third(s):
    for i in range(len(s))[1:]:
        if s[i-1] == s[i] and s[i] != 'e' and s[i] != 'o':
            return False
    return True

while True:
    tmp = input()
    if tmp == "end":
        break
    if first(tmp) and second(tmp) and third(tmp):
        print("<"+tmp+"> is acceptable.")
    else:
        print("<"+tmp+"> is not acceptable.")