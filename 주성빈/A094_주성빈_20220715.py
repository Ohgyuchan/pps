n = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croa:
  n = n.replace(i, '*')
print(len(n))
