while True :
    word = input()
    vowel = 'aeiou'
    previous = ''
    if word == 'end' :
        break
    flag = True
    vowelCount = 0
    vowelRepeat = 0
    consonantRepeat = 0
    
    for i in word :
        if i in vowel :
            consonantRepeat = 0
            vowelCount += 1
            vowelRepeat += 1
            if vowelRepeat > 2 :
                flag = False
            if previous == i :
                if i != 'e' and i != 'o' :
                    flag = False
        else :
            vowelRepeat = 0
            consonantRepeat += 1
            if consonantRepeat > 2 :
                flag = False
            if previous == i :
                flag = False
        
        previous = i
        
    if vowelCount < 1:
        flag = False

    if flag:
        print("<%s> is acceptable." % word)
    else:
        print("<%s> is not acceptable." % word)