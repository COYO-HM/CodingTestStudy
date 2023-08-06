# 세로 우승, 개수 조건 제대로 안 써서 지난 코드는 통과가 안 됐음
# 조건을 다 적용했는지 꼭 확인할 것
def solution(board):
    cnt_O, cnt_X = sum(row.count("O") for row in board), sum(row.count("X") for row in board)
    
    
    # 규칙을 지키지 않고 진행한 경우 => False
    check_cnt = cnt_O - cnt_X
    if not (check_cnt == 0 or check_cnt == 1):
        return 0
    
    # =========================================================
    # 우승 찾기
    # =========================================================
    # 가로 우승 찾기
    win_O, win_X = 0, 0
    for b in board:
        if b == "OOO": 
            win_O += 1
        elif b == "XXX": 
            win_X += 1
        
    # 세로 우승 찾기
    for i in range(len(board)):
        tmp = ""
        for j in range(len(board[0])):
            tmp += board[j][i]
        if tmp == "OOO":
            win_O += 1
        elif tmp == "XXX":
            win_X += 1
    
    # 대각선 기준 우승 찾기
    diagonal = ["".join(board[i][i] for i in range(3)), "".join(board[i][2 - i] for i in range(3))]
    for d in diagonal:
        if d == "OOO": 
            win_O += 1
        elif d == "XXX": 
            win_X += 1
    
    # =========================================================
    # o, x 개수 확인
    # =========================================================
    # 동시에 이긴 경우 => False
    if win_O == win_X and win_O > 0:
        return 0
    
    # O가 이기고 둘의 개수 차이가 1이 아닌 경우 => False
    if win_O == 1 and check_cnt != 1:
        return 0
    
    # X가 이기고 둘의 개수 차이가 0이 아닌 경우 => False
    if win_X == 1 and check_cnt != 0:
        return 0
            
        
    return 1
