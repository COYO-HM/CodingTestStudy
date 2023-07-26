# https://school.programmers.co.kr/learn/courses/30/lessons/181187
import math

def solution(r1, r2):
    cnt = 0

    # x좌표 기준으로 가능한 y좌표 탐색(제 1사분면만 탐색)
    for x in range(1, r2 + 1):
        # 가능한 y중 최솟값
        y_min = 0 if x >= r1 else math.ceil(math.sqrt(abs(r1 ** 2 - x ** 2)))
        # 가능한 y중 최댓값
        y_max = math.floor(math.sqrt(r2 ** 2 - x ** 2))
        cnt += y_max - y_min + 1

    return cnt * 4
