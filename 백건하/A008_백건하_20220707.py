n = int(input())

for _ in range(n):
    scores = list(map(int, input().split()))
    length = scores[0]
    scores = scores[1:]
    average = sum(scores) / length
    count = 0
    for score in scores:
        if score > average:
            count += 1
    
    print(f'{100.0 * count / length:.3f}%')