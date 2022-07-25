s = input()
ans = []
for c in s:
    if c == 'A' or c == 'B' or c == 'C':
        c = chr(ord(c)+26)
    ans.append(chr(ord(c)-3))
print(''.join(ans))

    