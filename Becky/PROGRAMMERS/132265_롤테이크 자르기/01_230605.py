# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/132265
from collections import Counter
def solution(topping):
    answer = 0
    second = Counter(topping) # 동생이 토핑을 전체 다 가진 경우부터 시작
    first = set()
    
    for i in topping:
        second[i] -= 1 # 동생 토핑 하나 뺏음
        
        if second[i] == 0: # 동생 토핑이 0개 되면 Counter에서 삭제
            del second[i]
            
        first.add(i) # 철수 토핑 추가
        
        if len(first) == len(second):
            answer += 1
            
    return answer