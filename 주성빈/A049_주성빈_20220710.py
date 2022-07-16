while True:
  pw = input()
  vowels = 'aeiou'
  f_check = 1
  s_check = 0

  if pw == 'end':
    break

  for i in pw:
    if i in vowels:
      f_check = 0
  if f_check == 0:
    for i in range(len(pw)-1):
      if pw[i] == pw[i+1] and pw[i] not in "eo":
        s_check = 1
  for i in range(len(pw)-2):
    if pw[i] in vowels and pw[i+1] in vowels and pw[i+2] in vowels:
      s_check = 1
    elif pw[i] not in vowels and pw[i+1] not in vowels and pw[i+2] not in vowels:
      s_check = 1

  if f_check == 0 and s_check == 0:
    print("<"+pw+"> is acceptable.")
  else:
    print("<"+pw+"> is not acceptable.")
