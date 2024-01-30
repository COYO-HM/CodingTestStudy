# https://www.acmicpc.net/problem/17484
# 18:00-18:27
import sys


def dfs(x, y, fuel, prev_direction):
    global min_fuel

    if x == N - 1:
        min_fuel = min(min_fuel, fuel)
        return

    for dx, dy in [(1, -1), (1, 0), (1, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and (dx, dy) != prev_direction:
            dfs(nx, ny, fuel + graph[nx][ny], (dx, dy))


N, M = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
min_fuel = float("inf")

for j in range(M):
    dfs(0, j, graph[0][j], (-1, -1))

print(min_fuel)
