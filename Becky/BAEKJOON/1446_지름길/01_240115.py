# https://www.acmicpc.net/problem/1446
# 20:29-21:11
import sys

input = sys.stdin.readline
N, D = map(int, input().rstrip().split())
shortcuts = [list(map(int, input().rstrip().split())) for _ in range(N)]

dp = [i for i in range(D + 1)]

for i in range(D + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)

    for s, e, d in shortcuts:
        if i == s and e <= D:
            dp[e] = min(dp[e], dp[i] + d)

print(dp[D])
