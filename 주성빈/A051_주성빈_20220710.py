dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = 0
for i in range(len(word)):
  for j in range(len(dial)):
    if word[i] in dial[j]:
      time += 3 + j

print(time)
