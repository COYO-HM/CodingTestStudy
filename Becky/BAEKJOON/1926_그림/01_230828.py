# https://www.acmicpc.net/problem/1926
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    que = deque([(x, y)])
    area = 1
    picture[x][y] = 0

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and picture[nx][ny] == 1:
                que.append((nx, ny))
                picture[nx][ny] = 0
                area += 1

    return area


N, M = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(N)]
cnt, max_area = 0, 0

for i in range(N):
    for j in range(M):
        if picture[i][j] == 1:
            cnt += 1
            area = bfs(i, j)
            max_area = max(max_area, area)

print(cnt)
print(max_area)