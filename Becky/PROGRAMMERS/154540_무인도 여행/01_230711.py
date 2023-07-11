# https://school.programmers.co.kr/learn/courses/30/lessons/154540
from collections import deque
def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0]) # row, column
    direction = [(1, 0), (-1, 0), (0, -1), (0, 1)] # dx, dy
    visited = [[False] * m for _ in range(n)] # 방문 여부 확인용
    
    for y in range(n):
        for x in range(m):
            if maps[y][x] == "X" or visited[y][x]: # 바다이거나 이미 방문한 경우
                continue
            
            q = deque() # 덱 생성
            q.append((y, x)) # 시작점 추가
            visited[y][x] = True # 방문 표시
            
            cost = 0
            while q:
                ny, nx = q.popleft()
                cost += int(maps[ny][nx]) # 입력이 str 타입 => 계산하기 위해 int로 형변환
                
                # 1) 지도 크기 넘지 않으면서 2) 방문 전이고 3) 바다 아닌 경우
                for dx, dy in direction:
                    if 0 <= ny + dy < n and 0 <= nx + dx < m and maps[ny+dy][nx+dx] != "X" and visited[ny+dy][nx+dx] == False:
                        q.append((ny+dy, nx+dx)) # 덱에 추가
                        visited[ny+dy][nx+dx] = True # 방문 표시
                        
            answer.append(cost)
                
    if answer: 
        answer.sort()
        return answer
    else:
        return [-1]
