import sys
input = sys.stdin.readline


n = int(input())
tree = list(map(int, input().split()))

tree.sort(reverse=True)

maxi = tree[0] + 2

for idx, val in enumerate(tree):
    candi = val + idx + 2
    if candi >= maxi:
        maxi = candi

print(maxi)