# https://school.programmers.co.kr/learn/courses/30/lessons/142085
from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e) # 최소힙 구현
        sumEnemy += e
        if sumEnemy > n: # 합이 n보다 큰 경우
            if k == 0:
                break
            sumEnemy += heappop(heap) # 힙에서 가장 적이 많은 경우를 pop
            k -= 1
        answer += 1
    return answer