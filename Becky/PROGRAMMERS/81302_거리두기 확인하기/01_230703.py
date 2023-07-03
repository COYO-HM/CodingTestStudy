# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque

def bfs(p, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(x, y, 0)]) # x, y 좌표, 거리
    visited = [[False] * 5 for _ in range(5)]
    visited[y][x] = True # 초기값 True
    
    while queue:
        x, y, distance = queue.popleft()
        
        if distance > 2:
            return True
        
        if distance > 0 and p[y][x] == 'P':
            return False
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[ny][nx] and p[ny][nx] != 'X':
                visited[ny][nx] = True
                queue.append((nx, ny, distance+1))
                
    return True

def solution(places):
    answer = []
    
    for p in places:
        safe = True
        
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    if not bfs(p, j, i):
                        safe = False
                        break
                        
        
        if safe: 
            answer.append(1)
        else: 
            answer.append(0)
        
        
    return answer
            
                