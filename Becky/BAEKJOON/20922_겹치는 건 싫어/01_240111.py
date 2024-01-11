# https://www.acmicpc.net/problem/20922
# 10:49-11:36
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
lst = list(map(int, input().rstrip().split()))
l, r = 0, 0

counter = [0] * (max(lst) + 1)
answer = 0

while r < N:
    if counter[lst[r]] < K:
        counter[lst[r]] += 1
        r += 1
    else:
        counter[lst[l]] -= 1
        l += 1
    answer = max(answer, r - l)

print(answer)
