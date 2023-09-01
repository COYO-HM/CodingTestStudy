# https://www.acmicpc.net/problem/10026
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, color, blind):
    que = deque([(x, y)])

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                next_color = graph[nx][ny]
                if blind and (color == "R" or color == "G"):
                    if next_color == "R" or next_color == "G":
                        que.append((nx, ny))
                        visited[nx][ny] = 1
                elif next_color == color:
                    que.append((nx, ny))
                    visited[nx][ny] = 1


N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

cnt = 0
blind_cnt = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            color = graph[i][j]
            bfs(i, j, color, False)
            cnt += 1

visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            color = graph[i][j]
            bfs(i, j, color, True)
            blind_cnt += 1

print(cnt, blind_cnt)
