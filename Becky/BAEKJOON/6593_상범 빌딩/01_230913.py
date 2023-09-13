# https://www.acmicpc.net/problem/6593
from collections import deque
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    que = deque([(start_floor, start_row, start_col, 0)])
    visited[start_floor][start_row][start_col] = 1

    while que:
        x, y, z, time = que.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if building[nx][ny][nz] == "E":
                    return "Escaped in " + str(time + 1) + " minute(s)."

                if not visited[nx][ny][nz] and building[nx][ny][nz] == ".":
                    visited[nx][ny][nz] = 1
                    que.append((nx, ny, nz, time + 1))
    return "Trapped!"


while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break

    graph = [[input() for _ in range(R + 1)] for _ in range(L)]
    building = [graph[i][:-1] for i in range(len(graph))]
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == "S":
                    start_floor, start_row, start_col = i, j, k

    print(bfs())
