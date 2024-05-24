# https://www.acmicpc.net/problem/4485
import sys
import heapq

input = sys.stdin.readline


def dijkstra(graph, N):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    start = (0, 0)

    distances = [[float('inf')] * N for _ in range(N)]
    distances[0][0] = graph[0][0]

    que = [(graph[0][0], start)]

    while que:
        curr_d, (x, y) = heapq.heappop(que)

        if curr_d > distances[x][y]:
            continue

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_d = curr_d + graph[nx][ny]
                if new_d < distances[nx][ny]:
                    distances[nx][ny] = new_d
                    heapq.heappush(que, (new_d, (nx, ny)))

    return distances[N - 1][N - 1]


number = 1
while True:
    N = int(input())
    if (N == 0):
        break

    graph = list(list(map(int, input().rstrip().split())) for _ in range(N))
    result = dijkstra(graph, N)

    print(f"Problem {number}: {result}")
    number += 1
