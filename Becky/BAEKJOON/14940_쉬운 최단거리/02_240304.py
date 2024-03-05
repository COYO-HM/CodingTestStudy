# https://www.acmicpc.net/problem/14940
# result 안 만들고 graph로만 계산하면 틀림
# 23:25-11:51
import sys
from collections import deque

n, m = map(int, input().split())
graph = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
visited = [[False] * m for _ in range(n)]
target = []
result = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            target.append(i)
            target.append(j)
            result[i][j] = 0
            visited[i][j] = True

        if graph[i][j] == 0:
            result[i][j] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    que = deque([target])
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                result[nx][ny] = result[x][y] + 1
                visited[nx][ny] = True
                que.append([nx, ny])


bfs()
for row in result:
    print(*row)
