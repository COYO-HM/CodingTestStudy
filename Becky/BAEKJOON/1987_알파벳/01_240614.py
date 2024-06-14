# https://www.acmicpc.net/problem/1987
# pypy3 통과
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, cnt):
    global res
    res = max(res, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            dfs(nx, ny, cnt + 1)
            visited.remove(board[nx][ny])  # 백 트래킹


input = sys.stdin.readline
R, C = map(int, input().split())
board = list(list(map(str, input().rstrip())) for _ in range(R))
visited = set(board[0][0])
res = 1

dfs(0, 0, 1)
print(res)
