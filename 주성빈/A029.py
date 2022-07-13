n = int(input())
f_way = int(input())
if n >= 6:
  print("Love is open door")
else:
  for i in range(n-1):
    f_way = int(not f_way)
    print(f_way)
