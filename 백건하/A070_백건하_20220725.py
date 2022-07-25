import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

card = deque([i for i in range(1, n+1)])

for i in range(n-1):
    card.popleft()
    card.append(card.popleft())

print(card[0])