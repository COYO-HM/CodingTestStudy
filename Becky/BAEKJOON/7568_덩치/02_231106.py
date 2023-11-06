# https://www.acmicpc.net/problem/7568
N = int(input())
peoples = [list(map(int, input().split())) for _ in range(N)]

ranks = [1] * N

for i in range(N):
    for j in range(N):
        if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
            ranks[i] += 1

print(*ranks)