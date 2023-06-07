# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0: # 아래로 이동
                x += 1
            elif i % 3 == 1: # 오른쪽으로 이동
                y += 1
            else: # 위로 이동
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    
    return sum(answer, [])