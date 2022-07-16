word = input()
string = []

for i in range(len(word)):
  if word[i] <= 'C':
    string.append(chr(ord(word[i])+23))
  else:
    string.append(chr(ord(word[i])-3))

print(''.join(string))
