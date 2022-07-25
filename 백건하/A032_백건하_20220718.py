T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    people = [[0] * (n+1) for _ in range(k+1)]
    
    for c in range(1, n+1):
        people[0][c] = c
    
    for r in range(1, k+1):
        for c in range(1, n+1):
            people[r][c] = sum(people[r-1][: c+1])

    print(people[k][n])