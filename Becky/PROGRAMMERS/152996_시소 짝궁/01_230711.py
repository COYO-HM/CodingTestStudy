# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/152996
from collections import Counter
def solution(weights):
    answer = 0
    counter = Counter(weights)
    min_weight = min(weights)
    max_weight = max(weights)

    for i in range(min_weight, max_weight+1):
        if counter[i] > 0:
            count_i = counter[i]
            answer += count_i * (count_i-1) // 2
            answer += count_i * counter[i * 3 / 2]
            answer += count_i * counter[i * 2]
            answer += count_i * counter[i * 4 / 3]

    return answer