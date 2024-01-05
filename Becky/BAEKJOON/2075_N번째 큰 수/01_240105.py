# https://www.acmicpc.net/problem/2075
# 10:47-11:25
# 메모리 제한이 있기 때문에 우선 순위 큐의 크기를 조정할 것
import sys
import heapq
N = int(input())
que = []

for _ in range(N):
    numbers = map(int, sys.stdin.readline().rstrip().split())
    for number in numbers:
        if len(que) < N:
            heapq.heappush(que, number)
        else:
            if que[0] < number:
                heapq.heappop(que)
                heapq.heappush(que, number)

print(que[0])