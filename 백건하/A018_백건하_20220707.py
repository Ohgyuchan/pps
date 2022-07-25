length = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A의 작은 숫자 순서대로 배열하기
A.sort()

B_with_idx = []
for idx, num in enumerate(B):
    B_with_idx.append([idx, num])

# B의 큰 숫자 순서대로 index 배열하기
B_with_idx.sort(key = lambda x: x[1], reverse=True)

# B의 가장 큰 숫자 index에 A의 가장 작은 값 넣기
A_reorder = [0] * length
for i in range(length):
    A_reorder[B_with_idx[i][0]] = A[i]

answer = 0
for i in range(length):
    answer += A_reorder[i] * B[i]

print(answer)
