# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12946
def hanoi(n, start, end, temp):
    if n == 1:
        return [[start, end]]
    else:
        # 1. n-1개의 원판을 start에서 temp로 옮김
        answer = hanoi(n-1, start, temp, end)
        
        # 2. 남은 1개의 가장 큰 원판을 start에서 end로 옮김
        answer.append([start, end])
        
        # 3. temp에 있는 n-1개의 원판을 end로 옮김
        answer += hanoi(n-1, temp, end, start)
        
        return answer

def solution(n):
    answer = hanoi(n, 1, 3, 2)
    return answer
