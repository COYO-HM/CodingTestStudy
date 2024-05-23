# https://www.acmicpc.net/problem/4485
import heapq
import sys
input = sys.stdin.readline

def dijkstra(cave, N):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    start = (0, 0)

    distances = [[float('inf')] * N for _ in range(N)]
    distances[0][0] = cave[0][0]

    que = [(cave[0][0], start)]

    while que:
        curr_distance, (x, y) = heapq.heappop(que)

        if curr_distance > distances[x][y]:
            continue

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:
                new_distance = curr_distance + cave[nx][ny]
                if new_distance < distances[nx][ny]:
                    distances[nx][ny] = new_distance
                    heapq.heappush(que, (new_distance, (nx, ny)))

    return distances[N - 1][N - 1]

number = 1
while True:
    N = int(input())
    if (N == 0):
        break

    cave = list(list(map(int, input().rstrip().split())) for _ in range(N))
    result = dijkstra(cave, N)

    print(f"Problem {number}: {result}")
    number += 1
