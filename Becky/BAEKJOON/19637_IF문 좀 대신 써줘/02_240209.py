# https://www.acmicpc.net/problem/19637
# 15:30-15:54
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
titles = []

for _ in range(N):
    name, hp = input().split()
    titles.append((int(hp), name))


for _ in range(M):
    hp = int(input())
    l, r = 0, N - 1

    while l <= r:
        mid = (l + r) // 2

        if titles[mid][0] < hp:
            l = mid + 1
        else:
            r = mid - 1

    print(titles[r + 1][1])