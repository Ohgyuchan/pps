import sys
n = int(sys.stdin.readline())
ans = []
cnt = 0
for i in range(n):
  command = sys.stdin.readline().split()
  if command[0] == 'push':
    ans.append(command[1])
  elif command[0] == 'pop':
    if len(ans) > cnt:
      print(ans[cnt])
      cnt += 1
    else:
      print(-1)
  elif command[0] == 'size':
    print(len(ans)-cnt)
  elif command[0] == 'empty':
    if len(ans) == cnt:
      print(1)
      cnt = 0
      ans = []
    else:
      print(0)
  elif command[0] == 'front':
    if len(ans) > cnt:
      print(ans[cnt])
    else:
      print(-1)
  elif command[0] == 'back':
    if len(ans) > cnt:
      print(ans[-1])
    else:
      print(-1)
