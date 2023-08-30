# https://www.acmicpc.net/problem/15486
# sys 안 쓰면 시간 초과 됨
import sys
N = int(input())
schedules = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0] * (N + 1)  # dp[i]: i번째 날까지 얻을 수 있는 최대 이익

for i in range(N - 1, -1, -1):
    if i + schedules[i][0] <= N:  # 상담이 퇴사일 이전에 끝날 때
        dp[i] = max(schedules[i][1] + dp[i + schedules[i][0]], dp[i + 1])
    else:  # 상담이 퇴사일 이후에 끝날 때
        dp[i] = dp[i + 1]

print(dp[0])
