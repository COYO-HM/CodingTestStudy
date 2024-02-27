# https://www.acmicpc.net/problem/1260
from collections import deque


def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")
    for i in range(1, N + 1):
        if not visited_dfs[i] and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    visited_bfs[v] = True
    que = deque([v])
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if not visited_bfs[i] and graph[v][i] == 1:
                que.append(i)
                visited_bfs[i] = True


N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = graph[e][s] = 1

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs(V)
print()
bfs(V)