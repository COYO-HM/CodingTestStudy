# https://www.acmicpc.net/problem/20922
# 5:15-5:29
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
lst = list(map(int, input().rstrip().split()))
l, r = 0, 0

C = [0] * (max(lst) + 1)
ans = 0

while r < N:
    if C[lst[r]] < K:
        C[lst[r]] += 1
        r += 1
    else:
        C[lst[l]] -= 1
        l += 1
    ans = max(ans, r - l)

print(ans)