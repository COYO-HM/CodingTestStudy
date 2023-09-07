# https://www.acmicpc.net/problem/4179
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while fire_que:
        x, y, time = fire_que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != "#" and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = time + 1
                fire_que.append((nx, ny, time + 1))

    while human_que:
        x, y, time = human_que.popleft()

        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            return time + 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != "#" and human_time[nx][ny] == -1 and (fire_time[nx][ny] == -1 or fire_time[nx][ny] > time + 1):
                human_time[nx][ny] = time + 1
                human_que.append((nx, ny, time + 1))

    return "IMPOSSIBLE"

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
fire_que, human_que = deque(), deque()
fire_time, human_time = [[-1] * C for _ in range(R)], [[-1] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if graph[i][j] == "J":
            human_que.append((i, j, 0))
            human_time[i][j] = 0
        elif graph[i][j] == "F":
            fire_que.append((i, j, 0))
            fire_time[i][j] = 0

result = bfs()
print(result)
