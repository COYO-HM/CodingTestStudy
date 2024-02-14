# https://www.acmicpc.net/problem/1927
import sys
from heapq import heappush, heappop

heap = []

for _ in range(int(input())):
    num = int(sys.stdin.readline())
    if num != 0:
        heappush(heap, num)
    else:
        if heap:
            p = heappop(heap)
            print(p)
        else:
            print(0)
