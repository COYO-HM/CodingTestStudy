# https://www.acmicpc.net/problem/8979
N, K = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]

nations.sort(key=lambda x: (-x[1], -x[2], -x[3]))

g, s, b = 0, 0, 0
for nation in nations:
    if nation[0] == K:
        g, s, b = nation[1], nation[2], nation[3]
        break

ranking = 1
for nation in nations:
    gold, silver, bronze = nation[1], nation[2], nation[3]
    if (gold > g or (gold == g and silver > s) or (gold == g and silver == s and bronze > b)):
        ranking += 1
    elif (gold, silver, bronze) < (g, s, b):
        break

print(ranking)
