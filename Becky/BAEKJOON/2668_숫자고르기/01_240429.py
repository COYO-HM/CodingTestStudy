# https://www.acmicpc.net/problem/2668
# 17:21-

def dfs(v, i):
    visited[v] = True
    w = lst[v]

    if not visited[w]:
        dfs(w, i)
    elif w == i:
        res.append(w)


N = int(input())
lst = [0] + [int(input()) for _ in range(N)]
res = []

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, i)

print(len(res))
res.sort()
for i in res:
    print(i)
