# 문제: https://www.acmicpc.net/problem/1699
n = int(input())
dp = [i for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, (i//2+1)):
        if (j**2)>i: # 제곱수가 i보다 크면 break
            break

        if dp[i] > dp[i-j**2] + 1: # 작은 수로 업데이트
            dp[i] = dp[i-j**2]+1
print(dp[n])
