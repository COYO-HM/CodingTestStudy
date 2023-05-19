# 문제: https://www.acmicpc.net/problem/10655
n = int(input())
checkpoint = [list(map(int, input().split())) for _ in range(n)]

# 1. 각 체크 포인트 사이의 거리 구하기
distance = []
for i in range(1, len(checkpoint)):
    d = abs(checkpoint[i][0]-checkpoint[i-1][0]) + abs(checkpoint[i][1]-checkpoint[i-1][1])
    distance.append(d)

# ================================