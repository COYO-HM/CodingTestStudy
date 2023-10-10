# https://www.acmicpc.net/problem/3190
from collections import deque

N = int(input())
board = [[0] * N for _ in range(N)]

# 사과 위치
for _ in range(int(input())):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2

# 뱀 회전 구간
snake_turn = deque()
for i in range(int(input())):
    x, c = input().split()
    if c == 'L':
        snake_turn.append([int(x), -1])
    else:
        snake_turn.append([int(x), 1])

# 게임 시작
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_d = 0
time = 0
snake = deque([(0, 0)])
snake_length = 1

while True:
    r, c = snake[0]
    if r >= N or c >= N or r < 0 or c < 0:
        time += 1
        break

    # 뱀 회전
    if snake_turn:
        x, c = snake_turn[0][0], snake_turn[0][1]  # 초, 방향
        if time == x:
            current_d = (current_d + c) % 4
            snake_turn.popleft()

    # 뱀 이동
    head_r, head_c = snake[0][0] + direction[current_d][0], snake[0][1] + direction[current_d][1]

    # 뱀이 자기 몸과 부딪히는 경우 게임 종료
    if (head_r, head_c) in snake or head_r >= N or head_c >= N or head_r < 0 or head_c < 0:
        time += 1
        break

    # 뱀 머리 이동
    snake.appendleft((head_r, head_c))

    # 사과 먹은 경우
    if board[head_r][head_c] == 2:
        board[head_r][head_c] = 0
        snake_length += 1
    else:   # 사과가 없는 경우
        snake.pop()

    time += 1

print(time)
