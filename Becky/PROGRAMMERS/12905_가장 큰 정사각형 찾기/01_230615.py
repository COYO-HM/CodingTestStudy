# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    answer = 0
    row = len(board) + 1
    col = len(board[0]) + 1

    dp = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(1, row):
        for j in range(1, col):
            if board[i - 1][j - 1] == 1:  # if board[i-1][j-1]: 로 써도 무방
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

                if dp[i][j] > answer:
                    answer = dp[i][j]

    return answer ** 2