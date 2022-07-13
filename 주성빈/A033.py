ans = []
for i in range(5):
  score = list(map(int, input().split()))
  ans.append(sum(score))

print(ans.index(max(ans))+1,max(ans), sep=' ')
