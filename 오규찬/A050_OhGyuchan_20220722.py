a = input()
# a = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
for i in a :
    ascii = (ord(i) - 3)
    if ascii < 65 :
        ascii = ascii + 26
    
    print(chr(ascii), end='')