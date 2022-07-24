seconds = 0
st = input()
for i in range(len(st)):
    tmp = ord(st[i])-65
    if tmp < 3:
        seconds += 3 
    elif tmp < 6:
        seconds += 4
    elif tmp < 9:
        seconds += 5
    elif tmp < 12:
        seconds += 6
    elif tmp < 15:
        seconds += 7
    elif tmp < 19:
        seconds += 8
    elif tmp < 22:
        seconds += 9
    elif tmp < 26:
        seconds += 10
print(seconds)