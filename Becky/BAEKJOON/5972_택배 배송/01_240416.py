# https://www.acmicpc.net/problem/5972
# 16:24-17:25
import heapq


def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))  # 거리, 시작점
    distance[start] = 0

    while que:
        d, curr = heapq.heappop(que)

        if distance[curr] < d:
            continue

        for v, w in graph[curr]:
            temp = d + w
            if temp < distance[v]:
                distance[v] = temp
                heapq.heappush(que, (temp, v))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [float("inf")] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)
print(distance[n])
