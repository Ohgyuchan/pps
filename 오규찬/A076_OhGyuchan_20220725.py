T = int(input())

for test_case in range(1, T + 1):
    t = int(input())
    answer = set()
    
    for i in range(t) :
        a = input()
        answer.add(a)
    print('#%d' % test_case)
    for i in sorted(answer, key=lambda x: (len(x), x)) :
        print(i)
