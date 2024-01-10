# https://www.acmicpc.net/problem/14940
# n, m 거꾸로 써서 틀림 레전드
# 10:24-11:35
import sys
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(target_x, target_y):
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                result[nx][ny] = result[x][y] + 1
                que.append((nx, ny))


n, m = map(int, input().split())
que = deque([])
graph = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
visited = [[False] * m for _ in range(n)]
result = [[-1] * m for _ in range(n)]

target_x, target_y = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            target_x, target_y = i, j
            que.append((i, j))
            visited[i][j] = True
            result[i][j] = 0

        if graph[i][j] == 0:
            result[i][j] = 0

bfs(target_x, target_y)

for row in result:
    print(*row)