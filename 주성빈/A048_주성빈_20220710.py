n = int(input())
cnt = n

for i in range(n):
  origin = input()
  for j in range(len(origin)-1):
    if origin[j] == origin[j+1]:
      pass
    elif origin[j] in origin[j+1:]:
      cnt -= 1
      break
    
print(cnt)
