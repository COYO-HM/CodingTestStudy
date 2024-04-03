# https://www.acmicpc.net/problem/16234
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    que.append((x, y))
    union = [(x, y)]
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    que.append((nx, ny))
                    union.append((nx, ny))

    if len(union) <= 1:
        return 0
    s = sum(graph[r][c] for r, c in union) // len(union)
    for r, c in union:
        graph[r][c] = s
    return 1


N, L, R = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(N))
que = deque([])
res = 0
while True:
    check = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                check += bfs(i, j)

    if check == 0:
        break
    res += 1
print(res)
