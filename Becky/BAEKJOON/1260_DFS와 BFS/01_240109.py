# https://github.com/psrom/CodingTestStudy
# 20:33-21:09
from collections import deque
def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")
    for i in range(1, N + 1):
        if visited_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    que = deque([v])
    visited_bfs[v] = 1
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if visited_bfs[i] == 0 and graph[v][i] == 1:
                que.append(i)
                visited_bfs[i] = 1


N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i][j] = graph[j][i] = 1

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs(V)
print()
bfs(V)
