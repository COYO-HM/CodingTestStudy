# https://www.acmicpc.net/problem/2531
# 16:02-16:17
import sys
from collections import deque

N, d, k, c = map(int, sys.stdin.readline().rstrip().split())
plates = list(int(input()) for _ in range(N))
que1 = deque(plates[:k])
que2 = deque(plates[k:])
ans = 0

for i in range(N):
    l = len(set(que1))

    if c in que1:
        ans = max(ans, l)
    else:
        ans = max(ans, l + 1)

    que2.append(que1.popleft())
    que1.append(que2.popleft())

print(ans)
