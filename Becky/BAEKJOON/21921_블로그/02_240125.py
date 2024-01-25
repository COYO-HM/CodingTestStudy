# https://www.acmicpc.net/problem/21921
# 16:45-17:15
import sys

input = sys.stdin.readline
N, X = map(int, input().rstrip().split())
visitors = list(map(int, input().rstrip().split()))
current_sum = sum(visitors[:X])

cnt_days = 1
max_visitor = current_sum
for i in range(X, N):
    current_sum = current_sum - visitors[i - X] + visitors[i]
    if current_sum > max_visitor:
        max_visitor = current_sum
        cnt_days = 1
    elif current_sum == max_visitor:
        cnt_days += 1

if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(cnt_days)
