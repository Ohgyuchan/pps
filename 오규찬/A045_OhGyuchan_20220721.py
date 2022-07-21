s = input().upper()

answer = [0] * 26

for i in s :
    answer[ord(i) - 65] += 1

if answer.count(max(answer)) > 1 :
    print('?')
else :
    print(chr(answer.index(max(answer)) + 65))
