N = int(input())
pts = []
for _ in range(N):
    [a,b] = map(int, input().split())
    pts.append([a,b])
    
pts.sort()
for i in range(len(pts)):
    print(pts[i][0], pts[i][1])

    