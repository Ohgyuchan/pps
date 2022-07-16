sentence = input()
arr_sentence = []

for i in range(len(sentence)):
  arr_sentence.append(sentence[i:])

for i in sorted(arr_sentence):
  print(i)
