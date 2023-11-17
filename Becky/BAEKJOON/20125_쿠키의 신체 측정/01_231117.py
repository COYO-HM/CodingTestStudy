# https://www.acmicpc.net/problem/20125
import sys
from collections import deque
N = int(input())
graph = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]


def find_heart():  # 심장 위치 찾기
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "*":
                return (i, j), (i + 1, j)


def find_waist(heart_x, heart_y):
    for i in range(heart_x + 1, N):
        if graph[i][heart_y] == "_":
            return (i - 1, heart_y), i - heart_x - 1  # 허리 끝나는 좌표, 허리 길이


def find_left_leg(waist_x, waist_y):
    for i in range(waist_x + 1, N):
        if graph[i][waist_y - 1] == "_":
            return i - waist_x - 1
    return N - waist_x - 1


def find_right_leg(waist_x, waist_y):
    for i in range(waist_x + 1, N):
        if graph[i][waist_y + 1] == "_":
            return i - waist_x - 1
    return N - waist_x - 1


head, heart = find_heart()
left_arm = graph[heart[0]][:heart[1]].count("*")
right_arm = graph[heart[0]][heart[1] + 1:].count("*")
waist_location, waist = find_waist(heart[0], heart[1])
left_leg = find_left_leg(waist_location[0], waist_location[1])
right_leg = find_right_leg(waist_location[0], waist_location[1])

print(heart[0] + 1, heart[1] + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)
