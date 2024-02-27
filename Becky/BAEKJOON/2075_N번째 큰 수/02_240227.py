# https://www.acmicpc.net/problem/2075
# 14:00-14:13
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(N):
    numbers = map(int, sys.stdin.readline().rstrip().split())
    for number in numbers:
        if len(heap) < N:
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heapreplace(heap, number)

print(heap[0])
