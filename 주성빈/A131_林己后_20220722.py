import sys
from collections import Counter
n = int(sys.stdin.readline())
ans = []
cnt = []
for i in range(n):
  ans.append(int(sys.stdin.readline()))

print(round(sum(ans)/len(ans)))

ans.sort()
print(ans[n//2])

cnt = Counter(ans).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
  print(cnt[1][0])
else:
  print(cnt[0][0])

print(max(ans)-min(ans))
