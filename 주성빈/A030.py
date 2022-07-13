n, now = map(int, input().split())
prob = list(map(float, input().split()))

good = [0 for i in range(n)]
bad = [0 for i in range(n)]

if now == 0:
  good[0] = prob[0]
  bad[0] = prob[1]

else:
  good[0] = prob[2]
  bad[0] = prob[3]

for i in range(1, n):
  good[i] = good[i-1]*prob[0] + bad[i-1]*prob[2]
  bad[i] = good[i-1]*prob[1] + bad[i-1]*prob[3]

print(round(good[n-1]*1000), round(bad[n-1]*1000), sep="\n")
