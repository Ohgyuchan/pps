temp_pri = int(input())
real_pri = 1000 - temp_pri
change = 0
coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
  change += real_pri // coin
  real_pri %= coin

print(change)
