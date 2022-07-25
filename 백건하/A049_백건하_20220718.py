while True:
    s = input()
    if s == 'end':
        break

    l = list(s)

    count_mo = 0
    mo = 0
    ja = 0
    is_acceptable = True
    for idx, val in enumerate(l):
        if idx != 0:
            if val == l[idx-1] and val not in ['e', 'o']:
                is_acceptable = False
                break
        
        if val in ['a', 'e', 'i', 'o', 'u']:
            count_mo += 1
            mo += 1
            ja = 0
            if mo == 3:
                is_acceptable = False
                break
        else:
            ja += 1
            mo = 0
            if ja == 3:
                is_acceptable = False
                break
    if count_mo == 0:
        is_acceptable = False

    if is_acceptable:
        print('<' + s + '> is acceptable.')
    else:
        print('<' + s + '> is not acceptable.')
