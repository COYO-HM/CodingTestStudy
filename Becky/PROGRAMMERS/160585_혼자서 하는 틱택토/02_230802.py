# https://school.programmers.co.kr/learn/courses/30/lessons/160585
# 정확성 51.9/100 더 떨어짐;

def solution(board):
    cnt_O, cnt_X = sum(row.count("O") for row in board), sum(row.count("X") for row in board)
    
    
    # 규칙을 지키지 않고 진행한 경우 => False
    check_cnt = cnt_O - cnt_X
    if not (check_cnt == 0 or check_cnt == 1):
        return 0
    
    
    # 열 기준 우승 찾기
    win_O, win_X = 0, 0
    for b in board:
        if b == "OOO": 
            win_O += 1
        elif b == "XXX": 
            win_X += 1
        
        
    # 대각선 기준 우승 찾기
    diagonal = ["".join(board[i][i] for i in range(3)), "".join(board[i][2 - i] for i in range(3))]
    for d in diagonal:
        if d == "OOO": 
            win_O += 1
        elif d == "XXX": 
            win_X += 1
    
    
    # 동시에 이긴 경우 => False
    if win_O == win_X and win_O > 0:
        return 0
            
        
    return 1