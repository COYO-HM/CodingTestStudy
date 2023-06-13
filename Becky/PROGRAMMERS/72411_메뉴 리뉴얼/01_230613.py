# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/72411
import itertools
def solution(orders, course):
    answer = []

    for c in course:
        dic = {}
        for order in orders:
            if len(order) < c:
                continue
            nCr = list(itertools.combinations(order, c))
            for n in nCr:
                l = ''.join(sorted(n))
                if l in dic:
                    dic[l] += 1
                else:
                    dic[l] = 1
        
        if len(dic.values()) == 0:
            m = 0
        else:
            m = max(dic.values())
        
        for i, v in dic.items():
            if v == m and m > 1:
                answer.append(i)

    answer.sort()
    return answer