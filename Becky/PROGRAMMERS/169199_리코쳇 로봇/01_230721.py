from collections import deque
 
def solution(board):
    answer = 0
    N, M = len(board), len(board[0])
    q = deque()
    visited = [[float('inf') for _ in range(M)] for _ in range(N)]
    
    # 로봇 시작 위치 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                visited[i][j] = 0
            
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while q:
        y, x, cnt = q.popleft()
        
        if board[y][x] == 'G':  # 목표위치 도달
            return cnt
        
        for dx, dy in directions:
            nx, ny = x, y
            
            # 미끄러져 이동
            while 0 <= ny + dy < N and 0 <= nx + dx < M and board[ny + dy][nx + dx] != 'D':
                nx += dx
                ny += dy
            
            # 이전에 해당 위치에 도달한 적이 없거나
            # 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우
            if visited[ny][nx] > cnt + 1:
                visited[ny][nx] = cnt + 1
                q.append((ny, nx, cnt + 1))
    
    return -1
