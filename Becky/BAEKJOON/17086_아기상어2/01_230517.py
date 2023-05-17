# 문제: https://www.acmicpc.net/problem/17086
from collections import deque

# 1. 입력 받기
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 2. 상어가 있는 좌표 저장
dq = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dq.append([i, j])

# 3. 최단 거리 구하기
d=[[-1, -1], [1, 1], [-1, 1], [1, -1],
   [0, 1], [0, -1], [1, 0], [-1, 0]]

while dq:
    x, y = dq.popleft()
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m: # 모서리
            continue

        if not graph[nx][ny]:
            graph[nx][ny] = graph[x][y] + 1
            dq.append([nx, ny])

# print(graph)
print(max(map(max, graph))-1)
