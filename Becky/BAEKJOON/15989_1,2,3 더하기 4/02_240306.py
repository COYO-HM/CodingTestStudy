# https://www.acmicpc.net/problem/15989
# 21:41-21:57
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for i in range(int(input())):
    n = int(input())
    print(dp[n])
