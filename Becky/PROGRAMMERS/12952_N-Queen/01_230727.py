# 퀸 배치 가능한지 체크 
# 1) 다른 열이고 2) 대각선 아니어야 함
def check_safe(lst, row, col):
    for r in range(row):
        if lst[r] == col or abs(lst[r] - col) == (row - r):
            return False
    return True


def dfs(lst, n, row):
    if n == row:  # 퀸 배치 완료
        return 1
    
    cnt = 0
    for col in range(n):
        if check_safe(lst, row, col):
            lst[row] = col  # index: row, value: column
            cnt += dfs(lst, n, row + 1)
    return cnt

def solution(n):
    queen = [0] * n
    return dfs(queen, n, 0)
