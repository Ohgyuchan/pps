num = int(input())

for _ in range(num) :
    expressions = list(map(str, input().split()))
    result = 0
    for i in range(len(expressions)) :
        if i == 0 :
            result += float(expressions[i])
        else:
            if expressions[i] == "#":
                result -= 7
            elif expressions[i] == "%":
                result += 5
            elif expressions[i] == "@":
                result *= 3
                
    print("%0.2f" % result)