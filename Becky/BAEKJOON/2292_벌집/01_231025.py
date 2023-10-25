# 문제: https://www.acmicpc.net/problem/2292
N = int(input())

room_number = 1
increment = 6
steps = 1

while room_number < N:
    room_number += increment
    increment += 6
    steps += 1

print(steps)