n = int(input())

def n_sum(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

a = []

for i in range(n) :
    s = input()
    a.append(s)

a.sort(key= lambda x: (len(x), n_sum(x), x))
print('\n'.join(a))