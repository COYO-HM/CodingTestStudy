# 문제: https://www.acmicpc.net/problem/6064
tc = int(input())
for t in range(tc):
    m, n, x, y = map(int, input().split())
    ans = 1
    while (x <= m*n):
        if x%n == y%n:
            print(x)
            ans = 0
            break
        x += m
    if ans:
        print(-1)
