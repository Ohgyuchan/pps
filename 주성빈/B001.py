## 입력
## 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
## 출력
## 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

input_1 = int(input()) # 컴퓨터 개수
input_2 = int(input()) # 몇개 입력?

arr = [[0] * input_1 for i in range(input_1)]
visited = [0 for i in range(input_1)]

for i in range(input_2):
  a, b = map(int, input().split())
  arr[a-1][b-1] = 1
  arr[b-1][a-1] = 1

def DFS(v):
  visited[v] = 1
  for i in range(input_1):
    if arr[v][i] == 1 and visited[i] == 0:
      DFS(i)

DFS(0)
count = 0
for i in range(1, input_1):
  if visited[i] == 1:
    count += 1

print(count)
