# https://www.acmicpc.net/problem/2512
# 13:38-13:53
import sys

input = sys.stdin.readline
N = int(input())
budgets = list(map(int, input().rstrip().split()))
M = int(input())

ans = 0
l, r = 0, max(budgets)
while l <= r:
    mid = (l + r) // 2
    current_sum = sum(min(mid, budget) for budget in budgets)

    if current_sum <= M:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
