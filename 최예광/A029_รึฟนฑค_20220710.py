N = int(input())
if N > 5:
    print("Love is open door")
else:
    first = int(input())
    for i in range(N-1):
        first = int(not first)
        print(first)
        