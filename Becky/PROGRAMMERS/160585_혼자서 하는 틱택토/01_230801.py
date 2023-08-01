# https://school.programmers.co.kr/learn/courses/30/lessons/160585
# 정확성 75.9/100

def check_board(board):
    def check_line(row, col, d_row, d_col):
        symbol = board[row][col]
        for _ in range(2):
            if not (0 <= row < 3 and 0 <= col < 3):
                return False
            if board[row][col] != symbol:
                return False
            row += d_row
            col += d_col
        return True

    for r in range(3):
        for c in range(3):
            if c <= 2 and check_line(r, c, 0, 1):  # 가로 라인 체크
                return 1
            if r <= 2 and check_line(r, c, 1, 0):  # 세로 라인 체크
                return 1
            if r == 0 and c <= 2 and check_line(r, c, 1, 1):  # 대각선 (왼쪽 상단에서 오른쪽 하단) 체크
                return 1
            if r == 2 and c <= 2 and check_line(r, c, -1, 1):  # 대각선 (왼쪽 하단에서 오른쪽 상단) 체크
                return 1
    return 0

def solution(board):
    count_O = 0
    count_X = 0
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "O":
                count_O += 1
            elif board[r][c] == "X":
                count_X += 1
                
    if count_O == 0 and count_X == 0:
        return 1
    elif count_X > count_O:
        return 0
    elif count_O >= 3 and count_O == count_X and check_board(board):
        return 0
    else:
        return check_board(board)
