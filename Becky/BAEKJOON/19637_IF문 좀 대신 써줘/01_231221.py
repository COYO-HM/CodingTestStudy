# https://www.acmicpc.net/problem/19637
# sys로 입력 안 받으면 통과가 안 되는 건데 삽질함
# 22:35 - 23:26

import sys
N, M = map(int, input().split())
level = [sys.stdin.readline().split() for _ in range(N)]


def binary_search(power):
    l, r = 0, len(level) - 1

    while l <= r:
        mid = (l + r) // 2
        if power > int(level[mid][1]):
            l = mid + 1
        else:
            r = mid - 1
    print(level[r + 1][0])


for _ in range(M):
    power = int(sys.stdin.readline().rstrip())
    binary_search(power)
    