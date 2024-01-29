# https://www.acmicpc.net/problem/19941
# 13:40-14:20
import sys
N, K = map(int, input().split())
lst = list(map(str, input().rstrip()))

ans = 0
for i in range(N):
    if lst[i] == "P":
        for j in range(max(0, i - K), min(i + K + 1, N)):
            if lst[j] == "H":
                lst[j] = "X"
                ans += 1
                break

print(ans)