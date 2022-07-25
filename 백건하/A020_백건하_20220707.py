candidates = []
people = 0

for i in range(4):
    outt, inn = map(int, input().split())
    people -= outt
    candidates.append(people)
    people += inn
    candidates.append(people)

print(max(candidates))
