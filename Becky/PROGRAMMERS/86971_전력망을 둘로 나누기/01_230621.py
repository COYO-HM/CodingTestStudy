from collections import deque
def bfs(start, graph):
    queue = deque([start])
    visited = [False] * len(graph)
    visited[start] = True
    cnt = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                cnt += 1
    
    return cnt


def solution(n, wires):
    graph = [[] for _ in range(n+1)] # 양방향 graph
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = float('inf')

    for v1, v2 in wires:
        graph[v1].remove(v2) # 연결 노드 끊음
        graph[v2].remove(v1) # 연결 노드 끊음
        cnt1 = bfs(v1, graph)
        cnt2 = n - cnt1 # v1과 연결되어 있지 않은 송전탑들
        
        diff = abs(cnt1 - cnt2)
        answer = min(answer, diff)
        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer
