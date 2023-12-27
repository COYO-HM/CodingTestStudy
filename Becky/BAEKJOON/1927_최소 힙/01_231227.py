# https://www.acmicpc.net/problem/1927
# 17:30 - 17:35
import sys
import heapq
operations = []
for _ in range(int(input())):
    operations.append(int(sys.stdin.readline().rstrip()))

heap = []

for op in operations:
    if op == 0:
        if not heap:
            print(0)
        else:
            min_val = heapq.heappop(heap)
            print(min_val)
    else:
        heapq.heappush(heap, op)
