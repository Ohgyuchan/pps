s = input()
s1 = s.upper()

letters = [0]*26
for c in s1:
    letters[ord(c)-65] += 1

if letters.count(max(letters)) > 1:
    print('?')
else:
    print(chr(letters.index(max(letters))+65))
