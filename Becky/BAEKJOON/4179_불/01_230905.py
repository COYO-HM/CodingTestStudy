# https://www.acmicpc.net/problem/4179
# 내일(9/6) 수정 예정
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, fire_x, fire_y):
    que = deque([(x, y, 0)])
    fire = deque([(fire_x, fire_y)])
    visited = [[False] * C for _ in range(R)]

    while que:
        x, y, time = que.popleft()
        visited[x][y] = True
        fire_x, fire_y = fire.popleft()

        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            return time + 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nx_fire = fire_x + dx[i]
            ny_fire = fire_y + dy[i]

            if 0 <= nx_fire < R and 0 <= ny_fire < C and graph[nx_fire][ny_fire] == ".":
                graph[nx_fire][ny_fire] = "F"
                fire.append((nx_fire, ny_fire))

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == "." and not visited[nx][ny]:
                que.append((nx, ny, time + 1))
                visited[nx][ny] = True

    return "IMPOSSIBLE"


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

start_x, start_y = 0, 0
fire_X, fire_Y = 0, 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == "J":
            start_x, start_y = i, j
        elif graph[i][j] == "F":
            fire_X, fire_Y = i, j

result = bfs(start_x, start_y, fire_X, fire_Y)
print(result)
