# https://www.acmicpc.net/problem/13549
# 14:41-15:48
import sys
from collections import deque

LIMIT = 100001
N, K = map(int, sys.stdin.readline().split())
time = [0] * LIMIT


def bfs(start, target):
    que = deque([start])

    while que:
        x = que.popleft()
        if x == target:
            return time[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < LIMIT and time[nx] == 0:
                if nx == x * 2 and nx != 0:
                    time[nx] = time[x]
                    que.appendleft(nx)
                else:
                    time[nx] = time[x] + 1
                    que.append(nx)

print(bfs(N, K))
