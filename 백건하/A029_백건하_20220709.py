n = int(input())
now = int(input())

answer = []
if n <= 5:
        for _ in range(n-1):
                now = 1-now
                answer.append(now)

        for one in answer:
                print(one)
else:
        print('Love is open door')
