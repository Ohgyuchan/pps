n = input()
cAlphabetCount = 0

if 'dz=' in n :
    cAlphabetCount += n.count('dz=')
    n = n.replace('dz=', ' ')

if 'z=' in n :
    cAlphabetCount += n.count('z=')
    n = n.replace('z=', ' ')

if 'd-' in n :
    cAlphabetCount += n.count('d-')
    n = n.replace('d-', ' ')

if 'c=' in n :
    cAlphabetCount += n.count('c=')
    n = n.replace('c=', ' ')

if 'c-' in n :
    cAlphabetCount += n.count('c-')
    n = n.replace('c-', ' ')

if 'lj' in n :
    cAlphabetCount += n.count('lj')
    n = n.replace('lj', ' ')

if 'nj' in n :
    cAlphabetCount += n.count('nj')
    n = n.replace('nj', ' ')

if 's=' in n :
    cAlphabetCount += n.count('s=')
    n = n.replace('s=', ' ')

print(cAlphabetCount + len(n.replace(' ', '')))