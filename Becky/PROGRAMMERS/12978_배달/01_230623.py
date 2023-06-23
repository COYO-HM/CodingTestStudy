import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, distance in graph[current_node]:
            new_distance = current_distance + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances

def solution(N, road, K):
    graph = {node: [] for node in range(1, N+1)}

    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))

    distances = dijkstra(graph, 1)

    count = sum(1 for distance in distances.values() if distance <= K)

    return count
