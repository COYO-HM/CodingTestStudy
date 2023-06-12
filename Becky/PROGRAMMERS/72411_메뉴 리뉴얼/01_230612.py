# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/72411
# tc 13~15 통과 안 됨
import itertools
def solution(orders, course):
    answer = []

    # 전체 알파벳 구하기
    s = ''.join(orders)
    s = list(set(s))
    s.sort()
    
    for c in course:
        nCr = list(itertools.combinations(s, c))
        
        lst = []
        for n in nCr:
            l = ''.join(n)
            lst.append(l)
            
        course_cnt = dict.fromkeys(lst, 0)
        
        for n in course_cnt:
            for order in orders:
                cnt = 0
                for i in range(len(n)):
                    if n[i] in order:
                        cnt += 1
                    if cnt == len(n):
                        course_cnt[n] += 1
        
        m = max(course_cnt.values())
        
        for i, v in course_cnt.items():
            if v == m and m > 1:
                answer.append(i)
    
    answer.sort()
    
    return answer