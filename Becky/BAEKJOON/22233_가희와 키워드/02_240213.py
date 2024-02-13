# https://www.acmicpc.net/problem/22233
# 22:55-23:05
import sys
N, M = map(int, input().split())
memo = set(sys.stdin.readline().rstrip() for _ in range(N))

for _ in range(M):
    keywords = set(sys.stdin.readline().rstrip().split(","))

    for k in keywords:
        memo.discard(k)

    print(len(memo))