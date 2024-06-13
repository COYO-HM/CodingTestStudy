# https://www.acmicpc.net/problem/1806

N, S = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, 0
curr_sum = 0
ans = float("inf")

while end < N:
    while curr_sum < S and end < N:
        curr_sum += lst[end]
        end += 1

    while curr_sum >= S:
        ans = min(ans, end - start)
        curr_sum -= lst[start]
        start += 1

print(0) if ans == float("inf") else print(ans)
