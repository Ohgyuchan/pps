s = input()

while True:
    if len(s) <= 10:
        break
    print(s[:10])
    s = s[10:]

if len(s) != 0:
    print(s)
