# https://www.acmicpc.net/problem/19941
# 7:28 - 8:04
import sys
N, K = map(int, input().split())
table = list(sys.stdin.readline().rstrip())
answer = 0

for i in range(N):
    if table[i] == "P":
        for j in range(max(i - K, 0), min(i + K + 1, N)):
            if table[j] == "H":
                table[j] = 0
                answer += 1
                break

print(answer)
