# 문제: https://www.acmicpc.net/problem/16967
h, w, x, y = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(h+x)]

A = [[0 for _ in range(w)] for _ in range(h)]

# 1. 계산 필요 없는 행렬
for i in range(x):
    for j in range(w):
        A[i][j] = lst[i][j]

for i in range(h):
    for j in range(y):
        A[i][j] = lst[i][j]

# 2. 계산 필요한 행렬
for i in range(x, h):
    for j in range(y, w):
        A[i][j] = lst[i][j] - A[i-x][j-y]

for l in A:
    print(*l)
